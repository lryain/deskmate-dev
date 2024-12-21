/**
* File: speechRecognizer.h
*
* Author: Lee Crippen
* Created: 12/06/16
*
* Description: Simple interface that various speech recognizer implementations can extend.
*
* Copyright: Anki, Inc. 2016
*
*/

#ifndef __Anki_AudioUtil_SpeechRecognizer_H_
#define __Anki_AudioUtil_SpeechRecognizer_H_

#include "audioUtil/audioDataTypes.h"
  
#include <functional>
#include <string>

namespace Anki {
namespace AudioUtil {
  
struct SpeechRecognizerCallbackInfo {
  std::string result;
  int startTime_ms;
  int endTime_ms;
  uint64_t startSampleIndex;
  uint64_t endSampleIndex;
  float score;
  
  const std::string Description() const;
};

struct SpeechRecognizerIgnoreReason {
  bool playback = false;
  bool notch = false;
  
  operator bool() const { return playback || notch; }
};
    
class SpeechRecognizer
{
public:
  SpeechRecognizer() = default;
  virtual ~SpeechRecognizer() { }
  SpeechRecognizer(const SpeechRecognizer&) = default;
  SpeechRecognizer& operator=(const SpeechRecognizer&) = default;
  SpeechRecognizer(SpeechRecognizer&& other) = default;
  SpeechRecognizer& operator=(SpeechRecognizer&& other) = default;
  
  using SpeechCallback = std::function<void(const SpeechRecognizerCallbackInfo& info)>;
  
  void SetCallback(SpeechCallback callback = SpeechCallback{} ) { _speechCallback = callback; }
  void Start();
  void Stop();
  
  virtual void Update(const AudioSample * audioData, unsigned int audioDataLen) = 0;
  
  using IndexType = int32_t;
  static constexpr IndexType InvalidIndex = -1;
  
  virtual void SetRecognizerIndex(IndexType index) { }
  virtual void SetRecognizerFollowupIndex(IndexType index) { }
  virtual IndexType GetRecognizerIndex() const { return InvalidIndex; }
  
protected:
  virtual void StartInternal() { }
  virtual void StopInternal() { }
  
  void DoCallback(const SpeechRecognizerCallbackInfo& info) const;
  
private:
  SpeechCallback _speechCallback;
  
}; // class SpeechRecognizer
    
} // end namespace AudioUtil
} // end namespace Anki

#endif // __Anki_AudioUtil_SpeechRecognizer_H_
