
set(SPEEXDSP_HOME "${LRYA_THIRD_PARTY_DIR}/speexdsp")

set(PLATFORM_DIR "")

if (MACOSX)
  set(PLATFORM_DIR "mac")
elseif (MATEOS)
  set(PLATFORM_DIR "mateos")
endif()

set(SPEEXDSP_LIB_PATH "${SPEEXDSP_HOME}/${PLATFORM_DIR}/lib")
set(SPEEXDSP_INCLUDE_PATHS "${SPEEXDSP_HOME}/${PLATFORM_DIR}/include")
set(SPEEXDSP_LIBS "speexdsp")

foreach(LIB ${SPEEXDSP_LIBS})
    add_library(${LIB} STATIC IMPORTED)
    set_target_properties(${LIB} PROPERTIES
        IMPORTED_LOCATION
        "${SPEEXDSP_LIB_PATH}/lib${LIB}.a"
        INTERFACE_INCLUDE_DIRECTORIES
        "${SPEEXDSP_INCLUDE_PATHS}")
    lrya_build_target_license(${LIB} "Xiph.org,${CMAKE_SOURCE_DIR}/licenses/speexdsp.license")
endforeach()
