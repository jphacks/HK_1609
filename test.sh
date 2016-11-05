#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`

python ./raspberrypi/camera/camera.py $DATE

MP4Box -fps 30 -add ./raspberrypi/camera/h264video/${DATE}.h264 ./raspberrypi/camera/mp4video/${DATE}.mp4

