# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from picamera import PiCamera
import sys
form time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

if __name__ == '__main__':
	args = sys.argv
	camera = PiCamera()
	camera.start_preview()
	#Turn on red LED
	GPIO.output(26, True)
	camera.start_recording('./../../DumpVideo'+args[1]+'.h264')
	sleep(10)
	camera.stop_recording()
	camera.stop_preview()
	#Turn off red LED
	GPIO.output(26, False)
	GPIO.cleanup()
