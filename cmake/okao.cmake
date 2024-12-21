set(OKAO_INCLUDE_PATH "${OKAO_VISION_DIR}/include")

set(WHOLE_ARCHIVE_FLAG "")
set(NO_WHOLE_ARCHIVE_FLAG "")

if (MATEOS)
  set(OKAO_LIB_PATH "${OKAO_VISION_DIR}/lib/Android/armeabi-v7a")
  set(WHOLE_ARCHIVE_FLAG "-Wl,--whole-archive")
  set(NO_WHOLE_ARCHIVE_FLAG "-Wl,--no-whole-archive")
elseif (MACOSX)
  set(OKAO_LIB_PATH "${OKAO_VISION_DIR}/lib/MacOSX")
else()
  message(FATAL_ERROR "OkaoVision not available for platform")
endif()



set(OKAO_LIBS
  ${WHOLE_ARCHIVE_FLAG}
  Okao      # Common
  OkaoCo    # Okao Common
  OkaoPc    # Property Estimation (for Smile/Gaze/Blink?)
  ${NO_WHOLE_ARCHIVE_FLAG}
  OkaoDt    # Dace Detection
  OkaoPt    # Face Parts Detection
  OkaoEx    # Facial Expression estimation
  OkaoFr    # Face Recognitioin
  OmcvPd    # Pet Detection
  OkaoSm    # Smile Estimation
  OkaoGb    # Gaze & Blink Estimation
)

foreach(LIB ${OKAO_LIBS})
  string(REGEX MATCH "^-" found ${LIB})
  if ("${found}" STREQUAL "-")
    # skip linker flags
    continue()
  endif()
  add_library(${LIB} STATIC IMPORTED)
  set_target_properties(${LIB} PROPERTIES
    IMPORTED_LOCATION
    "${OKAO_LIB_PATH}/libe${LIB}.a"
    INTERFACE_INCLUDE_DIRECTORIES
    "${OKAO_INCLUDE_PATH}")
  lrya_build_target_license(${LIB} "Commercial")
endforeach()
