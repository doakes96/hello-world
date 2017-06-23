# LED Pinout Test
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

pins = [17,18,27,6]

for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	for j in range(i+1):
		GPIO.output(pin,1)
		time.sleep(.8)
		GPIO.output(pin,0)
		time.sleep(.8)

GPIO.cleanup()
