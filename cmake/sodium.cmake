if (MATEOS)
  set(LIBSODIUM_INCLUDE_PATH "${LRYA_THIRD_PARTY_DIR}/libsodium/mateos/include")
  set(LIBSODIUM_LIB_PATH "${LRYA_THIRD_PARTY_DIR}/libsodium/mateos/lib")
elseif (MACOSX)
  set(LIBSODIUM_INCLUDE_PATH "${LRYA_THIRD_PARTY_DIR}/libsodium/mac/include")
  set(LIBSODIUM_LIB_PATH "${LRYA_THIRD_PARTY_DIR}/libsodium/mac/lib")
endif()

set(SODIUM_LIBS sodium)

add_library(sodium STATIC IMPORTED)

set_target_properties(sodium PROPERTIES
  IMPORTED_LOCATION "${LIBSODIUM_LIB_PATH}/libsodium.a"
  INTERFACE_INCLUDE_DIRECTORIES "${LIBSODIUM_INCLUDE_PATH}")
lrya_build_target_license(sodium "ISC,${CMAKE_SOURCE_DIR}/licenses/libsodium.license")
