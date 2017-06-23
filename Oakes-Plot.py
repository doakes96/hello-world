from matplotlib.pyplot import*
from numpy import* 

t = arange(1,3,0.02)
T = 6*log(t)-(7*e**(0.2*t))

figure(1)
clf()
plot(t,T)

xlabel('Time (minutes)')
ylabel('Temperature (celcuis)')
title('Oakes-plot')

savefig('Oakes_Plot.png', dpi = 300)

show()

print('Hello World! I just wrote my first Python Program. Yayyyyyyyy   		 Donald Oakes')

