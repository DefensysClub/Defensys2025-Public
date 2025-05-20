#!/bin/sh



APP_IP=$(getent hosts app | awk '{ print $1 }')
echo "executing entrypoint as $(whoami)"

export APPHOST=$APP_IP
echo "the app host is ${APPHOST}"
export APPURL="http://$APPHOST:8081"
exec node /home/bot/index.js