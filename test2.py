print (vars())

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print (vars())

from numpy import cos, sin, linspace
#print (vars())

#x = linspace(0, 7, 70) # solis = (7-0)/(70-1)
#x = linspace(0, 7, 71) # solis = (7-0)/(71-1)
x = linspace(0, 4, 11) 
y = cos(x)
y1 = sin(x)
#print (vars())

#from matplotlib import pyplot as plt
#plt.grid()
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.title('Funkcija $cos(x)$')
#plt.plot(x, y, 'bo')
#plt.plot(x, y, color= '#FF0000')
#plt.show()

from matplotlib import pyplot as plt
from numpy import sin
y2 = sin(x)
plt.plot(x,y2)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$$sin(x)$')
plt.plot(x, y, 'bo')
plt.plot(x, y, color= '#FF0000')
plt.plot(x, y1, 'go')
plt.plot(x, y, color= '#FF0000')
plt.legend(['$cos(x)$', '$sin(x)$', '$cos(x)$', 'sin(x)'])
plt.show()
