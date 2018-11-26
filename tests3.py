print (vars())

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print (vars())

from numpy import  sin, linspace
#print (vars())


x = linspace(0, 4, 11) 
y = sin(x)
y1 = x
#y2 = x-(x*x*x)/(1*2*3)
y2 = y1 - (x*x*x)/(1*2*3)
#y3= x - (x*x*x)/(1*2*3) + x*x*x*x*x*x/(1*2*3*4*5)
y3 = y2 + x**5/(1*2*3*4*5)
#y4=  x - (x*x*x)/(1*2*3) + x*x*x*x*x*x/(1*2*3*4*5)- x*x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
y4 = y3 - x**7//(1*2*3*4*5*6*7)
#print (vars())





from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$ un tās izvirzījumi rindā')
plt.plot(x, y, color='#FF0000')
plt.plot(x, y, color='#00FF00')
plt.plot(x, y, color='#0000FF')
plt.plot(x, y, color='#FFFF00')
plt.plot(x, y, color='#00FFFF')
plt.legend(['$sin(x)$', '$x$', '$x-x^3/3!$', '$x-x^3/3!+x^5/5!$', '$x-x^3/3!+x^5/5!+x^7/7!'])
plt.show()



