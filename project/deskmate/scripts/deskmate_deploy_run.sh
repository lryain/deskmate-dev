#!/usr/bin/env bash

GIT_PROJ_ROOT=`git rev-parse --show-toplevel`
${GIT_PROJ_ROOT}/project/deskmate/scripts/deskmate_stop.sh &&\
${GIT_PROJ_ROOT}/project/deskmate/scripts/deploy.sh &&\
${GIT_PROJ_ROOT}/project/deskmate/scripts/deskmate_restart.sh
