#Donald Oakes
#ECE 492
#06/07/2017
#Day 6 Problem 2

hours = input('How many hours did you work?  ')
rate = input('How much do you get paid per hour?  ')

if hours <= 40:
	gross_pay = (hours*rate)
	print 'Your gross pay is $', gross_pay

if hours > 40:
	gross_pay = (40*rate)+((hours-40)*(1.5*rate))
	print 'Your gross pay is $', gross_pay
