set(SIGNALESSENCE_EXTRA_INCLUDE_DIR "")
set(SIGNALESSENCE_LIB_PATH "")
set(SIGNALESSENCE_PLATFORM_DIR "")

if (MATEOS)
  set(SIGNALESSENCE_PLATFORM_DIR "mateos")
  set(SIGNALESSENCE_EXTRA_INCLUDE_DIR "cpu_arm")
elseif (MACOSX)
  set(SIGNALESSENCE_PLATFORM_DIR "mac")
  set(SIGNALESSENCE_EXTRA_INCLUDE_DIR "cpu_none")
endif()

# Signal Essence Lib Version
if (SE_V009)
  set(SIGNALESSENCE_VERSION_PATH "v009") # Updated prototype version with Echo Cancelation
  if (SE_HIGHRES)
    set(SIGNALESSENCE_PLATFORM_DIR "${SIGNALESSENCE_PLATFORM_DIR}-highres")
  endif(SE_HIGHRES)
else()
  set(SIGNALESSENCE_VERSION_PATH "v008") # Libs used in <= R 1.5
endif(SE_V009)

message(STATUS "Signal Essence lib ${SIGNALESSENCE_VERSION_PATH} type ${SIGNALESSENCE_PLATFORM_DIR}")

set(SIGNALESSENCE_HOME "${LRYA_THIRD_PARTY_DIR}/signalEssence/${SIGNALESSENCE_VERSION_PATH}")

set(SIGNALESSENCE_LIB_PATH "${SIGNALESSENCE_HOME}/${SIGNALESSENCE_PLATFORM_DIR}/platform/lrya_deskmate_example/build")

set(SIGNALESSENCE_PROJ_SRC "${SIGNALESSENCE_HOME}/${SIGNALESSENCE_PLATFORM_DIR}/project/lrya_deskmate")
set(SIGNALESSENCE_VAD_SRC "${SIGNALESSENCE_HOME}/${SIGNALESSENCE_PLATFORM_DIR}/project/lrya_deskmate_vad")

set(SIGNALESSENCE_INCLUDE_PATHS
  "${SIGNALESSENCE_PROJ_SRC}"
  "${SIGNALESSENCE_VAD_SRC}"
  "${SIGNALESSENCE_HOME}/${SIGNALESSENCE_PLATFORM_DIR}/se_lib_public"
  "${SIGNALESSENCE_HOME}/${SIGNALESSENCE_PLATFORM_DIR}/se_lib_public/${SIGNALESSENCE_EXTRA_INCLUDE_DIR}"
)

set(SIGNALESSENCE_LIBS
  mmfx
)

if (MATEOS)
  foreach(LIB ${SIGNALESSENCE_LIBS})
      add_library(${LIB} STATIC IMPORTED)
      set_target_properties(${LIB} PROPERTIES
          IMPORTED_LOCATION
          "${SIGNALESSENCE_LIB_PATH}/lib${LIB}.a"
          INTERFACE_INCLUDE_DIRECTORIES
          "${SIGNALESSENCE_INCLUDE_PATHS}"
          )

      lrya_build_target_license(${LIB} "Commercial")
  endforeach()
elseif (MACOSX)
  foreach(LIB ${SIGNALESSENCE_LIBS})
      add_library(${LIB} SHARED IMPORTED)
      set_target_properties(${LIB} PROPERTIES
          IMPORTED_LOCATION
          "${SIGNALESSENCE_LIB_PATH}/lib${LIB}.dylib"
          INTERFACE_INCLUDE_DIRECTORIES
          "${SIGNALESSENCE_INCLUDE_PATHS}"
          )

      lrya_build_target_license(${LIB} "Commercial")
  endforeach()
endif()
