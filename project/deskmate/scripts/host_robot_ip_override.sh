#!/usr/bin/env bash

function usage() {
  echo "$SCRIPT_NAME [OPTIONS]"
  echo "options:"
  echo "  -h                      print this message"
  echo "  -s LRYA_ROBOT_HOST      hostname or ip address of robot"
  echo ""
  echo "environment variables:"
  echo '  $LRYA_ROBOT_HOST        hostname or ip address of robot'
}

while getopts "hs:" opt; do
  case $opt in
    h)
      usage && exit 0
      ;;
    s)
      LRYA_ROBOT_HOST="${OPTARG}"
      shift 2
      ;;
    *)
      usage && exit 1
      ;;
  esac
done
