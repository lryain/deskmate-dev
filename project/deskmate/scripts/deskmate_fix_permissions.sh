#!/bin/bash
#
# Fix permissions on robot to match expected values required for access by non-root
# members of the lrya group.
#

set -e
set -u

# Get the directory of this script
SCRIPT_PATH=$(dirname $([ -L $0 ] && echo "$(dirname $0)/$(readlink -n $0)" || echo $0))
SCRIPT_NAME=$(basename ${0})
GIT=`which git`
if [ -z $GIT ]
then
    echo git not found
    exit 1
fi
TOPLEVEL=`$GIT rev-parse --show-toplevel`

source ${SCRIPT_PATH}/deskmate_env.sh ""

source ${SCRIPT_PATH}/host_robot_ip_override.sh ""

robot_set_host

# Remount rootfs read-write if necessary
MOUNT_STATE=$(\
    robot_sh "grep ' / ext4.*\sro[\s,]' /proc/mounts > /dev/null 2>&1 && echo ro || echo rw" \
)
[[ "$MOUNT_STATE" == "ro" ]] && robot_sh "/bin/mount -o remount,rw /"

robot_sh /bin/bash <<'EOT'
chown -R lrya:lrya /lrya
chmod ug+rw /lrya

test -f /data/etc/robot.pem && chown net:lrya /data/etc/robot.pem
chown -R net:lrya /data/mate-gateway

mkdir -p /data/data/com.lrya.deskmate
chmod -R 770 /data/data/com.lrya.deskmate
chown -R lrya:lrya /data/data/com.lrya.deskmate
EOT

[[ "$MOUNT_STATE" == "ro" ]] && robot_sh "/bin/mount -o remount,ro /"
