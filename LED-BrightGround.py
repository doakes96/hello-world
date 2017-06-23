#LED Brightness

import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if GPIO.input(led_pin) == False:
			print ("Button Pressed")
			time.sleep(0.5)
		
finally:
	print("Cleaning up")
	GPIO.cleanup() 
