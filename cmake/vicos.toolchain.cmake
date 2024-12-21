if(DEFINED MATEOS_TOOLCHAIN_HOME)
  set(mateos_root "$ENV{MATEOS_TOOLCHAIN_HOME}")
elseif(DEFINED ENV{MATEOS_TOOLCHAIN_HOME})
  set(mateos_root "$ENV{MATEOS_TOOLCHAIN_HOME}")
else()
  message(FATAL_ERROR "MATEOS_TOOLCHAIN_HOME not set. Define MATEOS_TOOLCHAIN_HOME in your environment")
endif()

set(target_triple "arm-oe-linux-gnueabi")

set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_CXX_COMPILER_ID Clang)

set(CMAKE_C_COMPILER "${mateos_root}/prebuilt/bin/arm-oe-linux-gnueabi-clang")
set(CMAKE_CXX_COMPILER "${mateos_root}/prebuilt/bin/arm-oe-linux-gnueabi-clang++")
set(CMAKE_LINKER "${mateos_root}/prebuilt/bin/arm-oe-linux-gnueabi-ld")

set(CMAKE_SYSROOT "${mateos_root}/sysroot")

set(CMAKE_CXX_FLAGS "-I${CMAKE_SYSROOT}/usr/include")

SET(CMAKE_FIND_ROOT_PATH ${CMAKE_SYSROOT})

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
