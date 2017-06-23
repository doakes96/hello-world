# Blink 123 integer choose
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
led_choice = 0
count = 0

import time

print "Choose an integer 1, 2, or 3."
led_choice = input()

if led_choice == 1:
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)

elif led_choice == 2:
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(6,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(6,GPIO.LOW)
		
elif  led_choice == 3:
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(6,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(6,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)

else: 
	print "ERROR: YOU HAVE ENTERNED AN INVAILD INTERGER!"


GPIO.cleanup()
