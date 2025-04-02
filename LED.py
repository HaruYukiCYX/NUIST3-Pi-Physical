#Author: Yuxuan Chen
#Date: 2025-03-31
#Title: LED.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(18,GPIO.LOW)
