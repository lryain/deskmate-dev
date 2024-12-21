set(FLATBUFFERS_INCLUDE_PATH "${LRYA_THIRD_PARTY_DIR}/flatbuffers/include")

set(FLATBUFFERS_LIBS
  flatbuffers
)

if (MATEOS)
  set(FLATBUFFERS_LIB_PATH "${LRYA_THIRD_PARTY_DIR}/flatbuffers/mateos")
elseif (MACOSX)
  set(FLATBUFFERS_LIB_PATH "${LRYA_THIRD_PARTY_DIR}/flatbuffers/mac/Release")
endif()

foreach(LIB ${FLATBUFFERS_LIBS})
  add_library(${LIB} STATIC IMPORTED)
  set_target_properties(${LIB} PROPERTIES
    IMPORTED_LOCATION
    "${FLATBUFFERS_LIB_PATH}/lib${LIB}.a"
    INTERFACE_INCLUDE_DIRECTORIES
    "${FLATBUFFERS_INCLUDE_PATH}")
  lrya_build_target_license(${LIB} "Apache-2.0,${CMAKE_SOURCE_DIR}/licenses/flatbuffers.license")
endforeach()
