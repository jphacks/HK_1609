# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

while GPIO.input(21)!=1:
    GPIO.output(26, True)
    time.sleep(0.5)
    GPIO.output(26, False)
    time.sleep(0.5)
GPIO.cleanup()
