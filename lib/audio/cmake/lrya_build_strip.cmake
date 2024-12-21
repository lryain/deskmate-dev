# This is coppied from tools/build/cmake

include(android_strip)
include(vicos_strip)

macro(anki_build_strip type target)
  if(ANDROID)
    android_strip(${type} ${target})
  elseif(VICOS)
    vicos_strip(${type} ${target})
  endif()
endmacro(anki_build_strip type target)
