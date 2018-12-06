# -*- coding: utf-8 -*-
from math import sin, fabs
from time import sleep

def f(x):
         return sin(x**2)
              
k = 0
a = 1
b = 4
 
funa = f(a)
funb = f(b)

if (funa * funb > 0.0 ):	
    print (" Dotajā intervālā [%s, %s] Sakņu nav " %(a,b))
    sleep(1); exit()
else:
    print ("Dotajā intervālā sakne(s) ir!")

deltax = 0.01

while ( fabs (b-a) > deltax ) :
    k = k+1
    x = (a+b)/2; funx = f(x)
    if (funa * funx < 0. ) :
        b = x
    else:
        a = x

print (" sin(x**2) sakne ir : ", x)
print (" f(x) = ", sin(x**2))
print (" Nepieciešamo iterāciju skaits intervālu dalīšanai uz pusēm: k= ",k)
