#!/usr/bin/env python
# coding: utf-8

import os
from twython import Twython
import sys

args = sys.argv

#twitter authentication
CONSUMER_KEY = 'ENTER YOUR CONSUMER_KEY'
CONSUMER_SECRET = 'ENTER YOUR CONSUMER_SECRET'
ACCESS_KEY = 'ENTER YOUR ACCESS_KEY'
ACCESS_SECRET = 'ENTER YOUR ACCESS_SECRET'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Do tweet
api.update_status(status= args[1]+'動画が投稿されたにゃ\n'+'https://www.youtube.com/watch?v='+args[2])
