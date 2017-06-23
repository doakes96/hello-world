#Quaddratic Equation Root solver

def roots(x,y,z):
	check = y**2-4*x*z
	if check<0:
		print'Error: The roots are complex with coeffiecnts of  ' + str(x) + ' and ' + str(y) + ' and ' + str(z)
	else:
		root1 = (check**.5-y)/(2*x)
		root2 = (-(check**.5)-y)/(2*x)
		print 'The roots of the equation ' + str(x) + 'x^2+ ' + str(y) + 'x+ ' + str(z) +' = 0 are ' + str(root1)+ ' and ' + str(root2)
	
roots(1,2,3)
roots(1,6,9)
roots(1,4,-3)


