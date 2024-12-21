set(SENSORY_HOME "${LRYA_THIRD_PARTY_DIR}/sensory")
set(SENSORY_INCLUDE_PATH "${SENSORY_HOME}/TrulyHandsfreeSDK/4.4.23/android/include")

if (MATEOS)
    set(SENSORY_LIB_PATH "${SENSORY_HOME}/TrulyHandsfreeSDK/4.4.23_noexpire/linux/arm-linux-gnueabi/lib")
elseif (MACOSX)
    set(SENSORY_LIB_PATH "${SENSORY_HOME}/TrulyHandsfreeSDK/4.4.23_noexpire/x86_64-darwin/lib")
endif()

set(SENSORY_LIBS
  thf
)

foreach(LIB ${SENSORY_LIBS})
  add_library(${LIB} STATIC IMPORTED)
  set_target_properties(${LIB} PROPERTIES
    IMPORTED_LOCATION
    "${SENSORY_LIB_PATH}/lib${LIB}.a"
    INTERFACE_INCLUDE_DIRECTORIES
    "${SENSORY_INCLUDE_PATH}")
  lrya_build_target_license(${LIB} "Commercial")
endforeach()
