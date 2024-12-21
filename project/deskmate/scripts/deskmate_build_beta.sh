#!/usr/bin/env bash

export GIT_PROJ_ROOT=`git rev-parse --show-toplevel`
${GIT_PROJ_ROOT}/project/deskmate/scripts/deskmate_build_shipping.sh \
                -DLRYA_BETA=1 \
                "$@"
