# -*- coding: utf-8 -*-

from picamera import PiCamera
import sys
form time import sleep

if __name__ == '__main__':
	args = sys.argv
	camera = PiCamera()
	camera.start_preview()
	camera.start_recording('/home/pi/DumpVideo/'+args[1]+'.h264')
	sleep(10)
	camera.stop_recording()
	camera.stop_preview()
