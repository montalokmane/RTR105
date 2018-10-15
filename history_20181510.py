Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> >>> print(123)
123
>>> print(85.3)
85.3
>>> print('Rudens')
Rudens
>>> x = 14
>>> y = 18
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 14, 'y': 18, '__name__': '__main__', '__doc__': None}
>>> x = 75
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 75, 'y': 18, '__name__': '__main__', '__doc__': None}
>>> ("mnemonic" = " memory aid")

SyntaxError: invalid syntax
>>> a = 35
>>> b = 14
>>> c = a * b
>>> print(c)
490
>>> hours = 45
>>> rate = 52
>>> pay = hours * rate
>>> print(pay)
2340
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * (1 - x)
>>> print(x)
-46.8
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> d = 1 + 2 ** 3/4 * 5
>>> print(d)
11
>>> kkk = 5+9
>>> print(kkk)
14
>>> mmm = 'hello' + 'there'
>>> print(mmm)
hellothere
>>> type()

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(mmm)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('welcome')
welcome
>>> inp = input('Europe floor?')
Europe floor?

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    inp = input('Europe floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    usf = int(inp) + 1
NameError: name 'inp' is not defined
>>> # count word frequency
>>> counts = dict()
>>> for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

		

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    for line in handle:
NameError: name 'handle' is not defined
>>> x = 5
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print('Smaller')

	
Smaller
>>> 
