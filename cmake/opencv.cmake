if(MATEOS)
  set(OPENCV_3RDPARTY_LIB_DIR ${LRYA_THIRD_PARTY_DIR}/opencv/mateos/3rdparty/lib)

  set(OPENCV_LIB_DIR ${LRYA_THIRD_PARTY_DIR}/opencv/mateos/lib)

  set(OPENCV_INCLUDE_PATHS
      ${LRYA_THIRD_PARTY_DIR}/opencv
      ${LRYA_THIRD_PARTY_DIR}/opencv/mateos
      ${LRYA_THIRD_PARTY_DIR}/opencv/mateos/include)

else()
  set(OPENCV_3RDPARTY_LIB_DIR ${LRYA_THIRD_PARTY_DIR}/opencv/mac/3rdparty/lib/Release)

  set(OPENCV_LIB_DIR ${LRYA_THIRD_PARTY_DIR}/opencv/mac/lib/Release)

  set(OPENCV_INCLUDE_PATHS ${LRYA_THIRD_PARTY_DIR}/opencv/mac)

endif()

set(OPENCV_LIBS
    calib3d
    features2d
    imgproc 
    core
    highgui
    objdetect
    video
    flann
    imgcodecs
    ml
    videoio)

# Static libs for mac, shared for android
set(LIB_EXT a)
set(LIB_TYPE STATIC)
set(LIB_POSTFIX "")
if(MATEOS)
  set(LIB_EXT so)
  set(LIB_TYPE SHARED)
  set(LIB_POSTFIX .3.4)
endif()

# Add the include directory for each OpenCV module:
foreach(OPENCV_MODULE ${OPENCV_LIBS})
  add_library(${OPENCV_MODULE} ${LIB_TYPE} IMPORTED)

  set(MODULE_INCLUDE_PATH "${LRYA_THIRD_PARTY_DIR}/opencv/modules/${OPENCV_MODULE}/include")

  set(include_paths
      ${MODULE_INCLUDE_PATH}
      ${OPENCV2_INCLUDE_PATH})

  set_target_properties(${OPENCV_MODULE} PROPERTIES
                        IMPORTED_LOCATION
                        ${OPENCV_LIB_DIR}/libopencv_${OPENCV_MODULE}.${LIB_EXT}${LIB_POSTFIX}
                        INTERFACE_INCLUDE_DIRECTORIES
                        "${include_paths}")
  lrya_build_target_license(${OPENCV_MODULE} "BSD-4,${CMAKE_SOURCE_DIR}/licenses/opencv.license")

  list(APPEND OPENCV_INCLUDE_PATHS ${MODULE_INCLUDE_PATH})

endforeach()

add_library(opencv_interface INTERFACE IMPORTED)
set_target_properties(opencv_interface PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES
    "${OPENCV_INCLUDE_PATHS}"
)

if(MATEOS)
  set(OPENCV_EXTERNAL_LIBS
      libpng
      libtiff
      #cpufeatures # missing for mateos build?
      libjpeg) # NOT using turbo jpeg below
else()
  set(OPENCV_EXTERNAL_LIBS
      IlmImf
      libjasper
      libpng
      libtiff
      zlib
      libjpeg
      ippicv
      ippiw
      ittnotify)
endif()

foreach(LIB ${OPENCV_EXTERNAL_LIBS})
    add_library(${LIB} STATIC IMPORTED)
    set_target_properties(${LIB} PROPERTIES
        IMPORTED_LOCATION
        ${OPENCV_3RDPARTY_LIB_DIR}/lib${LIB}.a)
endforeach()

lrya_build_target_license(libpng "libpng,${CMAKE_SOURCE_DIR}/licenses/libpng.license")
lrya_build_target_license(libtiff "ISC,${CMAKE_SOURCE_DIR}/licenses/libtiff.license")
lrya_build_target_license(libjpeg "BSD-3-like,${CMAKE_SOURCE_DIR}/licenses/libjpeg-turbo.license")

if(MACOSX)
    lrya_build_target_license(IlmImf "BSD-3,${CMAKE_SOURCE_DIR}/licenses/openexr.license")
    lrya_build_target_license(libjasper "BSD-2,${CMAKE_SOURCE_DIR}/licenses/libjasper.license")
    lrya_build_target_license(ippicv  "BSD-3,${CMAKE_SOURCE_DIR}/licenses/ipp.license")
    lrya_build_target_license(ippiw  "BSD-3,${CMAKE_SOURCE_DIR}/licenses/ipp.license")
    lrya_build_target_license(ittnotify  "BSD-3,${CMAKE_SOURCE_DIR}/licenses/ittnotify.license")
endif()

message(STATUS "including OpenCV, [Modules: ${OPENCV_LIBS}], [3rdParty: ${OPENCV_EXTERNAL_LIBS}]")

list(APPEND OPENCV_LIBS ${OPENCV_EXTERNAL_LIBS})

if (MACOSX)
  # Add Frameworks
  find_library(ACCELERATE Accelerate)
  find_library(APPKIT AppKit)
  find_library(OPENCL OpenCL)
  list(APPEND OPENCV_LIBS ${ACCELERATE} ${APPKIT} ${OPENCL})
endif()

# On Android, we need to copy shared libs to our library output folder
macro(copy_opencv_android_libs)
if(MATEOS)
  if (TARGET copy_opencv_libs)
      return()
  endif()
  
  set(INSTALL_LIBS
    "${OPENCV_LIBS}")
  
  message(STATUS "opencv libs: ${INSTALL_LIBS}")
  
  set(OUTPUT_FILES "")
  
  foreach(lib ${INSTALL_LIBS})
      get_target_property(LIB_PATH ${lib} IMPORTED_LOCATION)
      get_filename_component(LIB_FILENAME ${LIB_PATH} NAME)
      set(DST_PATH "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/${LIB_FILENAME}") 
      message(STATUS "copy opencv lib: ${lib} ${LIB_PATH} -> ${DST_PATH}")
      add_custom_command(
          OUTPUT "${DST_PATH}"
          COMMAND ${CMAKE_COMMAND}
          ARGS -E copy_if_different "${LIB_PATH}" "${DST_PATH}"
          COMMENT "copy ${LIB_PATH}"
          VERBATIM
      )
      list(APPEND OUTPUT_FILES ${DST_PATH})
  endforeach() 
  
  add_custom_target(copy_opencv_libs ALL DEPENDS ${OUTPUT_FILES})

endif()
endmacro()

