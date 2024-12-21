#
# gen-version.cmake
#
# Copyright Anki, Inc. 2018
#
# Generates a files containing info in  <build>/etc/{version,revision}

#
# <build>/etc/version
#

#
# The version number format is:
#
# X.Y.Z<build_type>[_<build_tag>]
# 
# X = major version
# Y = minor version
# Z = incremental build number
# build_type = dev (d) or empty (release)
# build_tag = optional tag specifier for build

# read base version from VERSION file
file(READ ${CMAKE_SOURCE_DIR}/VERSION BASE_VERSION)
string(STRIP ${BASE_VERSION} BASE_VERSION)

# LRYA_BUILD_VERSION  contains the build counter
set(LRYA_BUILD_VERSION 0)
if (DEFINED ENV{LRYA_BUILD_VERSION})
    set(LRYA_BUILD_VERSION $ENV{LRYA_BUILD_VERSION})
endif()

# default to "dev" build flavor
set(LRYA_BUILD_TYPE "d")
if (${CMAKE_BUILD_TYPE} STREQUAL "Release")
    set(LRYA_BUILD_TYPE "")
endif()

# if LRYA_BUILD_TAG is defined, append it to the version number with `_` prefex
set(LRYA_BUILD_TAG "")
if (DEFINED ENV{LRYA_BUILD_TAG})
    set(LRYA_BUILD_VERSION "_$ENV{LRYA_BUILD_TAG}")
endif()

configure_file(${CMAKE_SOURCE_DIR}/templates/cmake/version.in
               ${CMAKE_BINARY_DIR}/etc/version
               @ONLY)


#
# <build>/etc/revision
#

# if LRYA_BUILD_DESKMATE_REV contains the git revision, use it
set(LRYA_BUILD_DESKMATE_REV "")
if (DEFINED ENV{LRYA_BUILD_DESKMATE_REV})
    set(LRYA_BUILD_DESKMATE_REV $ENV{LRYA_BUILD_DESKMATE_REV})
else()
    execute_process(
      COMMAND git rev-parse --short HEAD
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
      OUTPUT_VARIABLE LRYA_BUILD_DESKMATE_REV
      OUTPUT_STRIP_TRAILING_WHITESPACE
    )
endif()

configure_file(${CMAKE_SOURCE_DIR}/templates/cmake/revision.in
               ${CMAKE_BINARY_DIR}/etc/revision
               @ONLY)

# Set the DESKMATE_COMPAT_VERSION from the file
file(READ ${CMAKE_SOURCE_DIR}/DESKMATE_COMPAT_VERSION DESKMATE_COMPAT_VERSION)
string(STRIP ${DESKMATE_COMPAT_VERSION} DESKMATE_COMPAT_VERSION)

configure_file(${CMAKE_SOURCE_DIR}/templates/cmake/deskmate-compat-version.in
               ${CMAKE_BINARY_DIR}/etc/deskmate-compat-version
               @ONLY)
