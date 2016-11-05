#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`

python ./raspberrypi/camera/camera.py $DATE

MP4Box -fps 30 -add ./raspberrypi/camera/h264video/${DATE}.h264 ./raspberrypi/camera/mp4video/${DATE}.mp4

ID=`python ./raspberrypi/youtube/upload_video.py --file="./raspberrypi/camera/mp4video/${DATE}.mp4" --title="${DATE}" --description="Had a great time surfing in Santa Cruz" --keywords="${DATE}" --category="22" --privacyStatus="private"`


python ./raspberrypi/twitter/twitter.py $DATE $ID
