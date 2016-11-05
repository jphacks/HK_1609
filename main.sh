#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`

python /home/pi/cameraTest/camera.py $DATE

MP4Box -fps 30 -add /home/pi/DumpVideo/${DATE}.h264 /home/pi/VideoLogs/${DATE}.mp4

dropbox_uploader.sh -k upload ./VideoLogs/${DATE}.mp4 /HackVideo/${DATE}.mp4
