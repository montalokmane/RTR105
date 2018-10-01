Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __b

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __b
NameError: name '__b' is not defined
>>> __builtins__
<module '__builtin__' (built-in)>
>>> __builtins__.doc__

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    __builtins__.doc__
AttributeError: 'module' object has no attribute 'doc__'
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(builtins__.__doc__)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(builtins__.__doc__)
NameError: name 'builtins__' is not defined
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> c = 'w'
>>> vars()
{'c': 'w', '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> a * a

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a * a
NameError: name 'a' is not defined
>>> type(a)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> a='w'
>>> type(a)
<type 'str'>
>>> b='w'
>>> type(b)
<type 'str'>
>>> 
