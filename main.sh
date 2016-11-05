#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`

python ./raspberrypi/camera/camera.py $DATE

MP4Box -fps 30 -add ./DumpVideo/${DATE}.h264 ./Video/${DATE}.mp4

dropbox_uploader.sh -k upload ./Video/${DATE}.mp4 /HackVideo/${DATE}.mp4

python ./raspberrypi/twitter/twitter.py $DATE
