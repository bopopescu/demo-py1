#generator - fun used to generate values

def testMyGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

for i in testMyGenerator():
    print(i)

def testMyGenerator():
    yield 'r'
    yield 'a'
    yield 'j'
    yield 'ji'

'''
for i in testMyGenerator():
    print(i)
'''
gnrobj = testMyGenerator()
print(gnrobj)
print(gnrobj.__next__())

'''
>>> gnrobj.__next__()
'r'
>>> gnrobj.__next__()
'a'
>>> gnrobj.__next__()
'j'
>>> gnrobj.__next__()
'ji'
>>> gnrobj.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

'''