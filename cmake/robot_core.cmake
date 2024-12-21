if (MATEOS)
  if(NOT TARGET robot_core)

  file(GLOB ROBOT_CORE_SRCS ${CMAKE_SOURCE_DIR}/robot/core/src/*.c)
  file(GLOB ROBOT_CORE_INCS ${CMAKE_SOURCE_DIR}/robot/core/inc/*.h)

  set(ROBOT_CORE_LIBS
    robot_core
  )

  foreach(LIB ${ROBOT_CORE_LIBS})
    add_library(${LIB} STATIC
      ${ROBOT_CORE_SRCS}
      ${ROBOT_CORE_INCS}
    )

    target_include_directories(${LIB} 
      PRIVATE
      $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/robot/core/inc>
    )

    target_link_libraries(${LIB}
      PRIVATE
      gpio
    )

    set_target_properties(${LIB} PROPERTIES
      INTERFACE_INCLUDE_DIRECTORIES
      "${CMAKE_SOURCE_DIR}/robot/core/inc"
    )
    lrya_build_target_license(${LIB} "LRYA")

  endforeach()
endif()
endif()
