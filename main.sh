#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`

python ./raspberrypi/camera/camera.py $DATE

MP4Box -fps 30 -add ./DumpVideo/${DATE}.h264 ./Video/${DATE}.mp4

ID=`python upload_video.py --file="/Users/violuka/documents/HK_1609/testvideo/201605230058.mp4" --title="Summer vacation in California" --description="Had a great time surfing in Santa Cruz" --keywords="surfing,Santa Cruz" --category="22" --privacyStatus="private"`


python ./raspberrypi/twitter/twitter.py $DATE $ID
