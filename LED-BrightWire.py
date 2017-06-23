#LED Input with wire Day 7
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 21
led_pin2 = 12
led_pin3 = 16
cont = 1

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

pwm_led = GPIO.PWM(led_pin1,500)
pwm_led.start(10)
duty = 50


while cont ==1:
	if GPIO.input(led_pin2) == False:
		pressed1 = 1
		print ('Button Pressed. Brightness increasing.')
		
		while duty < 100:
			duty = duty + 5
			pwm_led.ChangeDutyCycle(duty)
			time.sleep(.2)
			
	if GPIO.input(led_pin3) == False:
		pressed2 = 2
		print ('Button Pressed. Britness decreasing.')
		
		while duty > 0:
			duty = duty -5
			pwm_led.ChangeDutyCycle(duty)
			time.sleep(.2)
			
	if GPIO.input(led_pin2) == False and GPIO.input(led_pin3) == False:
		cont = 0
		
GPIO.cleanup()
			
