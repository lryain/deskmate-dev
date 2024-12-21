#
# This file is intended to be included in other scripts that need to communicate with the robot
#

#
# SSH/SCP support
#

: ${LRYA_ROBOT_USER:="root"}

robot_set_host ()
{
    if [ -z ${LRYA_ROBOT_HOST+x} ]; then
        GIT_PROJ_ROOT=`git rev-parse --show-toplevel`
        ROBOT_IP_FILE="${GIT_PROJ_ROOT}/robot_ip.txt"
        if [ ! -f $ROBOT_IP_FILE ]; then
            echo "ERROR: Missing file $ROBOT_IP_FILE"
            echo "You can create this file manually"
            echo "The file just needs to contain the robot's IP address"
            exit
        fi
        LRYA_ROBOT_HOST=$(cat $ROBOT_IP_FILE)
    fi
}

robot_sh ()
{
    if [ -z ${LRYA_ROBOT_HOST} ]; then
        echo "ERROR: Unspecified robot host."
        return 1
    fi
    ssh ${LRYA_ROBOT_USER}@${LRYA_ROBOT_HOST} $*
    return $?
}

robot_cp ()
{
    if [ -z ${LRYA_ROBOT_HOST} ]; then
        echo "ERROR: Unspecified robot host"
        return 1
    fi

    if [ $# -eq 3 ]; then
        ARGS="$1"
        shift
    else
        ARGS=""
    fi

    SRC="$1"
    DST=$LRYA_ROBOT_USER@$LRYA_ROBOT_HOST:"$2"

    scp ${ARGS} ${SRC} ${DST}
    return $?
}

robot_cp_from ()
{
    if [ -z ${LRYA_ROBOT_HOST} ]; then
        echo "ERROR: Unspecified robot host"
        return 1
    fi

    if [ $# -eq 3 ]; then
        ARGS="$1"
        shift
    else
        ARGS=""
    fi

    SRC=$LRYA_ROBOT_USER@$LRYA_ROBOT_HOST:"$1"
    DST="$2"

    scp ${ARGS} ${SRC} ${DST}
    return $?
}
