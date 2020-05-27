
def testyield():
    yield 1
...
>>> for i in testyield():
...     print(i)
...
1
>>> def testyield():
...     yield 1
...     yield 2
...     yield 3
...     yield 4
...
>>> for i in testyield():
...     print(i)
...
1
2
3
4
>>> def testyield():
...     return 1
...
>>> for i in testyield():
...     print(i)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> type(testyield())
<class 'int'>
>>> def testyield():
...     yield 1
...
>>> type(testyield())
<class 'generator'>
'''
'''