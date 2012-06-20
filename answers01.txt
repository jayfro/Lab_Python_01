ben@ben:~$ python
Python 2.7.3 (default, Apr 20 2012, 22:44:07) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "----------Exercise 1----------"
----------Exercise 1----------
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> 56thnumber
  File "<stdin>", line 1
    56thnumber
             ^
SyntaxError: invalid syntax
>>> length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'length' is not defined
>>> !Tayo
  File "<stdin>", line 1
    !Tayo
    ^
SyntaxError: invalid syntax
>>> NUMBER
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NUMBER' is not defined
>>> Android_phone1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Android_phone1' is not defined
>>> this variable
  File "<stdin>", line 1
    this variable
                ^
SyntaxError: invalid syntax
>>> print "----------Exercise 2----------"
----------Exercise 2----------
>>> a=False
>>> type(a)
<type 'bool'>
>>> b=3.7
>>> type(b)
<type 'float'>
>>> c='Alex'
>>> type(c)
<type 'str'>
>>> d=7
>>> type(d)
<type 'int'>
>>> e='True'
>>> type(e)
<type 'str'>
>>> f=17
>>> type(f)
<type 'int'>
>>> g='17
  File "<stdin>", line 1
    g='17
        ^
SyntaxError: EOL while scanning string literal
>>> h=True
>>> type(h)
<type 'bool'>
>>> i='3.14159'
>>> type(i)
<type 'str'>
>>> j="---add---"
>>> type(j)
<type 'str'>
>>> a=False
>>> b=True
>>> c=False
>>> b and c
False
>>> b or c
True
>>> not a and b
True
>>> (a and b)or not c
True
>>> not b and not (a or c)
False
>>> not ((not b or not a) and c) or a
True
>>> print "----------Exercise 3----------"
----------Exercise 3----------
>>> 5/2
2
>>> 5/2.0
2.5
>>> 5.0/2
2.5
>>> 7*(1/2)
0
>>> 7* (1/2.0)
3.5
>>> 5**2
25
>>> 5.0**2
25.0
>>> 5**2.0
25.0
>>> 1/3
0
>>> 1/3.0
0.3333333333333333

