#f = open('/home/prave/Documents/myfile.txt','w')
#f.write('Hey this is my first file, hi how are you? \n hey this is new line')
'''
f = open('/home/prave/Documents/myfile.txt','r')
print(f.read())

f = open('/home/prave/Documents/myfile.txt','r+')
f.tell()
0
f.seek(7)
7
f.write('$$$$$$$$$$$$$$')
14
f.read()
'file, hi how are you? \n hey this is new line'
f.seek(0)
0
f.read()
f = open('/home/prave/Documents/myfile.txt','w')
f.write('new one ')
8
f.close()
f = open('/home/prave/Documents/myfile1.txt','a')

f = open('/home/prave/Documents/myfile.txt','a+')
f.tell()
8
f = open('/home/prave/Documents/myfile.txt','r+')
f.tell()
0
f = open('/home/prave/Documents/myfile.txt','w+')
f.tell()
0
f = open('/home/prave/Documents/myfile.txt','w+')
f.closed
False
f.close()
f.closed
True
with open('/home/prave/Documents/myfile.txt') as f:
...     data = f.read()
...
f.closed
True
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

f = open('/home/prave/Documents/myfile.txt','r')
f.readlines()[0]
'Hey this is my first file, hi how are you? \n'
f = open('/home/prave/Documents/myfile.txt','r')
f.readlines(1)
['Hey this is my first file, hi how are you? \n']
f = open('/home/prave/Documents/myfile.txt','r')
f.read()
'Hey this is my first file, hi how are you? \n hey this is new line'
'''
f = open('/home/prave/Documents/myfile.txt','a')
f.tell()