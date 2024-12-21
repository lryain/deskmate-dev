// CC0 Public Domain: http://creativecommons.org/publicdomain/zero/1.0/
//
// Simple C++11 Signal System
//
// Source: https://testbit.eu/~timj/blogstuff/simplesignal.cc
// https://testbit.eu/cpp11-signal-system-performance/
// https://testbit.eu/pub/docs/rapicorn/latest/aidasignal_8hh_source.html
//
#ifndef __SIMPLE_SIGNAL_HH__
#define __SIMPLE_SIGNAL_HH__

#include "simpleSignal_fwd.h"

#include <unistd.h>
#include <assert.h>
#include <stdint.h>
#include <functional>
#include <memory>
#include <vector>

namespace Signal {

  namespace Lib {

    /// ProtoSignal is the template implementation for callback list.
    template<typename,typename> class ProtoSignal;   // undefined

    /// CollectorInvocation invokes signal handlers differently depending on return type.
    template<typename,typename> struct CollectorInvocation;

    /// CollectorLast returns the result of the last signal handler from a signal emission.
    template<typename Result>
    struct CollectorLast {
      typedef Result CollectorResult;
      explicit        CollectorLast ()              : last_() {}
      inline bool     operator()    (Result r)      { last_ = r; return true; }
      CollectorResult result        ()              { return last_; }
    private:
      Result last_;
    };

    /// CollectorDefault implements the default signal handler collection behaviour.
    template<typename Result>
    struct CollectorDefault : CollectorLast<Result>
    {};

    /// CollectorDefault specialisation for signals with void return type.
    template<>
    struct CollectorDefault<void> {
      typedef void CollectorResult;
      void                  result     ()           {}
      inline bool           operator() (void)       { return true; }
    };

    /// CollectorInvocation specialisation for regular signals.
    template<class Collector, class R, class... Args>
    struct CollectorInvocation<Collector, R (Args...)> {
      inline bool
      invoke (Collector &collector, const std::function<R (Args...)> &cbf, Args... args)
      {
        return collector (cbf (args...));
      }
    };

    /// CollectorInvocation specialisation for signals with void return type.
    template<class Collector, class... Args>
    struct CollectorInvocation<Collector, void (Args...)> {
      inline bool
      invoke (Collector &collector, const std::function<void (Args...)> &cbf, Args... args)
      {
        cbf (args...); return collector();
      }
    };

    class HandleBase
    {
    public:
      virtual ~HandleBase() {}
      virtual void Unlink() = 0;
    };

    class ScopedHandleContainer
    {
    public:
      ScopedHandleContainer(HandleBase* handle) : _handle(handle) {}
      ~ScopedHandleContainer() { _handle->Unlink(); delete _handle; }
    private:
      HandleBase* _handle;
    };

    /// ProtoSignal template specialised for the callback signature and collector.
    template<class Collector, class R, class... Args>
    class ProtoSignal<R (Args...), Collector> : private CollectorInvocation<Collector, R (Args...)> {
    protected:
      typedef std::function<R (Args...)> CbFunction;
      typedef typename CbFunction::result_type Result;
      typedef typename Collector::CollectorResult CollectorResult;
    private:
      /// ProtoHandle maintains a handle to this signal
      class ProtoHandle : public HandleBase {
      public:
        virtual void Unlink() {
          if (_heartbeatRef.lock()) {
            _subject->Unsubscribe(_link);
          }
        }
        ProtoHandle(ProtoSignal<R (Args...), Collector>* signalOwner, size_t signalId, std::shared_ptr<void> heartbeat)
          : _subject(signalOwner)
          , _link(signalId)
          , _heartbeatRef(heartbeat)
        {}
        virtual ~ProtoHandle() {}
      private:
        ProtoSignal<R (Args...), Collector>* _subject;
        size_t _link;
        std::weak_ptr<void> _heartbeatRef;
      };

      /// SignalLink implements a doubly-linked ring with ref-counted nodes containing the signal handlers.
      struct SignalLink {
        SignalLink *next, *prev;
        CbFunction  function;
        int         ref_count;
        explicit    SignalLink (const CbFunction &cbf) : next (NULL), prev (NULL), function (cbf), ref_count (1) {}
        /*dtor*/   ~SignalLink ()           { assert (ref_count == 0); }
        void        incref     ()           { ref_count += 1; assert (ref_count > 0); }
        void        decref     ()           { ref_count -= 1; if (!ref_count) delete this; else assert (ref_count > 0); }
        void
        unlink ()
        {
          function = NULL;
          if (next)
            next->prev = prev;
          if (prev)
            prev->next = next;
          decref();
          // leave intact ->next, ->prev for stale iterators
        }
        size_t
        add_before (const CbFunction &cb)
        {
          SignalLink *link = new SignalLink (cb);
          link->prev = prev; // link to last
          link->next = this;
          prev->next = link; // link from last
          prev = link;
          static_assert (sizeof (link) == sizeof (size_t), "sizeof size_t");
          return size_t (link);
        }
        bool
        deactivate (const CbFunction &cbf)
        {
          if (cbf == function)
          {
            function = NULL;      // deactivate static head
            return true;
          }
          for (SignalLink *link = this->next ? this->next : this; link != this; link = link->next)
            if (cbf == link->function)
            {
              link->unlink();     // deactivate and unlink sibling
              return true;
            }
          return false;
        }
        bool
        remove_sibling (size_t id)
        {
          for (SignalLink *link = this->next ? this->next : this; link != this; link = link->next)
            if (id == size_t (link))
            {
              link->unlink();     // deactivate and unlink sibling
              return true;
            }
          return false;
        }
      };
      SignalLink   *callback_ring_; // linked ring of callback nodes
      std::shared_ptr<void> heartbeat_; // for observers to tell if this signal is still alive
      /*copy-ctor*/ ProtoSignal (const ProtoSignal&) = delete;
      ProtoSignal&  operator=   (const ProtoSignal&) = delete;
      void
      ensure_ring ()
      {
        if (!callback_ring_)
        {
          callback_ring_ = new SignalLink (CbFunction()); // ref_count = 1
          callback_ring_->incref(); // ref_count = 2, head of ring, can be deactivated but not removed
          callback_ring_->next = callback_ring_; // ring head initialization
          callback_ring_->prev = callback_ring_; // ring tail initialization
        }
      }

      /// Function to remove a signal handler through its connection ID, returns if a handler was removed.
      bool Unsubscribe(size_t connection) { return callback_ring_ ? callback_ring_->remove_sibling (connection) : false; }
      friend class ProtoHandle;
    public:
      /// ProtoSignal constructor, connects default callback if non-NULL.
      ProtoSignal (const CbFunction &method) :
      callback_ring_ (NULL),
      heartbeat_( (void*)0x12345678, [] (void*) {} ) // pointer isn't actually valid, so give deleter that won't delete anything
      {
        if (method != NULL)
        {
          ensure_ring();
          callback_ring_->function = method;
        }
      }
      /// ProtoSignal destructor releases all resources associated with this signal.
      ~ProtoSignal ()
      {
        if (callback_ring_)
        {
          while (callback_ring_->next != callback_ring_)
            callback_ring_->next->unlink();
          assert (callback_ring_->ref_count >= 2);
          callback_ring_->decref();
          callback_ring_->decref();
        }
      }

      /// Function to add a new function or lambda as signal handler.
      /// This returns a smart handle to the connection.
      /// ***YOUR CALLBACK WILL BE UNREGISTERED WHEN THIS HANDLE IS DESTROYED.***
      /// If you call this function and don't store the return value, you're almost certainly doing it wrong.
      /// This handle can also be manually unsubscribed by assigning it nullptr.
      SmartHandle ScopedSubscribe(const CbFunction &cb) __attribute__((warn_unused_result)) {
        ensure_ring();
        return SmartHandle(new ScopedHandleContainer(new ProtoHandle(this, callback_ring_->add_before(cb), heartbeat_)));
      }

      /// Add callback to this signal dispatcher. If the signal dispatcher ever emit()s after your callback
      /// is no longer valid, very bad things will happen. ScopedSubscribe (above) is recommended.
      void SubscribeForever(const CbFunction &cb) {
        ensure_ring();
        callback_ring_->add_before(cb);
      }

      /// Emit a signal, i.e. invoke all its callbacks and collect return types with the Collector.
      CollectorResult
      emit (Args... args)
      {
        Collector collector;
        if (!callback_ring_)
          return collector.result();
        SignalLink *link = callback_ring_;
        link->incref();
        do
        {
          if (link->function != NULL)
          {
            const bool continue_emission = this->invoke (collector, link->function, args...);
            if (!continue_emission)
              break;
          }
          SignalLink *old = link;
          link = old->next;
          link->incref();
          old->decref();
        }
        while (link != callback_ring_);
        link->decref();
        return collector.result();
      }
    };

  } // Lib
  // namespace Simple

  /**
   * Signal is a template type providing an interface for arbitrary callback lists.
   * A signal type needs to be declared with the function signature of its callbacks,
   * and optionally a return result collector class type.
   * Signal callbacks can be added with operator+= to a signal and removed with operator-=, using
   * a callback connection ID return by operator+= as argument.
   * The callbacks of a signal are invoked with the emit() method and arguments according to the signature.
   * The result returned by emit() depends on the signal collector class. By default, the result of
   * the last callback is returned from emit(). Collectors can be implemented to accumulate callback
   * results or to halt a running emissions in correspondance to callback results.
   * The signal implementation is safe against recursion, so callbacks may be removed and
   * added during a signal emission and recursive emit() calls are also safe.
   * The overhead of an unused signal is intentionally kept very low, around the size of a single pointer.
   * Note that the Signal template types is non-copyable.
   */
  template <typename SignalSignature, class Collector = Lib::CollectorDefault<typename std::function<SignalSignature>::result_type> >
  struct Signal /*final*/ :
  Lib::ProtoSignal<SignalSignature, Collector>
  {
    typedef Lib::ProtoSignal<SignalSignature, Collector> ProtoSignal;
    typedef typename ProtoSignal::CbFunction             CbFunction;
    /// Signal constructor, supports a default callback as argument.
    Signal (const CbFunction &method = CbFunction()) : ProtoSignal (method) {}
  };

  /// This function creates a std::function by binding @a object to the member function pointer @a method.
  template<class Instance, class Class, class R, class... Args> std::function<R (Args...)>
  slot (Instance &object, R (Class::*method) (Args...))
  {
    return [&object, method] (Args... args) { return (object .* method) (args...); };
  }

  /// This function creates a std::function by binding @a object to the member function pointer @a method.
  template<class Class, class R, class... Args> std::function<R (Args...)>
  slot (Class *object, R (Class::*method) (Args...))
  {
    return [object, method] (Args... args) { return (object ->* method) (args...); };
  }

  /// Keep signal emissions going while all handlers return !0 (true).
  template<typename Result>
  struct CollectorUntil0 {
    typedef Result CollectorResult;
    explicit                      CollectorUntil0 ()      : result_() {}
    const CollectorResult&        result          ()      { return result_; }
    inline bool
    operator() (Result r)
    {
      result_ = r;
      return result_ ? true : false;
    }
  private:
    CollectorResult result_;
  };

  /// Keep signal emissions going while all handlers return 0 (false).
  template<typename Result>
  struct CollectorWhile0 {
    typedef Result CollectorResult;
    explicit                      CollectorWhile0 ()      : result_() {}
    const CollectorResult&        result          ()      { return result_; }
    inline bool
    operator() (Result r)
    {
      result_ = r;
      return result_ ? false : true;
    }
  private:
    CollectorResult result_;
  };
  
  /// CollectorVector returns the result of the all signal handlers from a signal emission in a std::vector.
  template<typename Result>
  struct CollectorVector {
    typedef std::vector<Result> CollectorResult;
    const CollectorResult&        result ()       { return result_; }
    inline bool
    operator() (Result r)
    {
      result_.push_back (r);
      return true;
    }
  private:
    CollectorResult result_;
  };
} // Simple

#endif // __SIMPLE_SIGNAL_HH__