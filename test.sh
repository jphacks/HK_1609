#!/bin/sh
DATE=`date +'%Y%m%H%M%S'`
ID=`python ./raspberrypi/youtube/upload_video.py --file="/Users/violuka/documents/HK_1609/testvideo/201605230058.mp4" --title="Summer vacation in California" --description="Had a great time surfing in Santa Cruz" --keywords="surfing,Santa Cruz" --category="22" --privacyStatus="public"
`

python ./raspberrypi/twitter/twitter.py $DATE $ID
