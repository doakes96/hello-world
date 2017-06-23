#Midterm question 5

coefficients = []
num_coe = int(raw_input('How many coefficients are there?  '))
x = int(raw_input('What do you want x to be?  '))

for a in range(num_coe):
	a1 = raw_input('What are the coefficients in order from highest to lowest?  ')
	coefficients.append(a1)
	
def poly(x,coefficients):
	n = len(coefficients)
	value = 0
	ans = 0
	for i in range(0,n):
		value = coefficients[i]
		ans =(ans + int(value*(x**i)))
		print (ans)
		print (value)
		

print 
print 'Evaluated Polynomial:'
print
print 'The answer is - ',poly(x,a1)
