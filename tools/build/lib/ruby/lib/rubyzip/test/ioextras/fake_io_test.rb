require 'test_helper'
require 'zip/ioextras'

class FakeIOTest < MiniTest::Unit::TestCase
  class FakeIOUsingClass
    include ::Zip::IOExtras::FakeIO
  end

  def test_kind_of?
    obj = FakeIOUsingClass.new

    assert(obj.kind_of?(Object))
    assert(obj.kind_of?(FakeIOUsingClass))
    assert(obj.kind_of?(IO))
    assert(!obj.kind_of?(Fixnum))
    assert(!obj.kind_of?(String))
  end
end
