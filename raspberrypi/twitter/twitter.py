#!/usr/bin/env python
# coding: utf-8

import os
from twython import Twython
import sys

args = sys.argv

#twitter authentication
CONSUMER_KEY = 'IFMXZ9BqqWVTmX8srd0WalFBk'
CONSUMER_SECRET = 'bRF1LweheqbpFXUw53E4n8RsmFxtvsOprdfIkuvQEsdNzXlOMM'
ACCESS_KEY = '794768347095134208-n1ab71hhTrjX2SVCnJ4Ut4vWgvt8cKo'
ACCESS_SECRET = 'RCBHf2SIbiOnSuf0a54bdLXA3j4dbdV48XCng9WlsIM7L'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


# Do tweet
api.update_status(status= args[1]+':動画が投稿されたにゃ')
