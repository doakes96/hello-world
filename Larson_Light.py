#LED Larson Light
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = [4,17,18,27]

for pin in led_pin:
	print 'Setup Pins'
	GPIO.setup(pin, GPIO.OUT)
	
count = 0
step = 1
stepcount = 4

seq = []
seq = list(range(0,stepcount))
seq[0] = [1,0,0,0]
seq[1] = [0,1,0,0]
seq[2] = [0,0,1,0]
seq[3] = [0,0,0,1]

while True:
	print ("-- Step: "+ str(count) + " --")
	for pinref in range(0,4):
		pinout = led_pin[pinref]
		if seq[count][pinref]!=0:
			print(" Enabled " + str(pinout))
			GPIO.output(pinout, True)
		else:
			print(" Disabled "+str(pinout))
			GPIO.output(pinout, False)
		
	count += step
		
	if (count == stepcount) or (count<0):
		step = step * -1
		count = count + step + step
		
	time.sleep(.3)
		
GPIO.cleanup()
