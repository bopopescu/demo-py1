# 7 deque
"""
>>> from collections import deque
>>> myq = deque()
>>> myq.append(11)
>>> myq.append(12)
>>> myq.append(13)
>>> myq
deque([11, 12, 13])
>>> mylist  = [1,2,3,4,5]
>>> mylist.pop()
5
>>>
>>> mylist.pop()
4
>>> mylist
[1, 2, 3]
>>> myq.popleft()
11
>>> myq
deque([12, 13])
>>> myq.appendleft(101)
>>> myq
deque([101, 12, 13])
>>> myq.pop()
13
>>> myq
deque([101, 12])
>>> import collections
>>> mydict1 = {'a':11,'b':12}
>>> mydict2 = {'c':13,'d':14}
>>> chain = collections.ChainMap(mydict1,mydict2)
>>> chain
ChainMap({'a': 11, 'b': 12}, {'c': 13, 'd': 14})
>>> chain.maps
[{'a': 11, 'b': 12}, {'c': 13, 'd': 14}]
>>> chain.keys
<bound method Mapping.keys of ChainMap({'a': 11, 'b': 12}, {'c': 13, 'd': 14})>
>>> chain['a']
11
>>> chain['ac']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python3.6/collections/__init__.py", line 883, in __getitem__
    return self.__missing__(key)            # support subclasses that define __missing__
  File "/usr/lib64/python3.6/collections/__init__.py", line 875, in __missing__
    raise KeyError(key)
KeyError: 'ac'
>>> chain['c']
13
>>> mydict3 = {'c':13,'d':14}
>>> chain.new_chile(mydict3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ChainMap' object has no attribute 'new_chile'
>>> chain.new_child(mydict3)
ChainMap({'c': 13, 'd': 14}, {'a': 11, 'b': 12}, {'c': 13, 'd': 14})
>>> chain['c']
13
>>> mydict3 = {'c':33,'d':14}
>>> chain.new_child(mydict3)
ChainMap({'c': 33, 'd': 14}, {'a': 11, 'b': 12}, {'c': 13, 'd': 14})
>>> chain['c']
13
>>> chain['c']
13
>>> chain.keys()
KeysView(ChainMap({'a': 11, 'b': 12}, {'c': 13, 'd': 14}))
>>> chain.values()
ValuesView(ChainMap({'a': 11, 'b': 12}, {'c': 13, 'd': 14}))
>>> list(chain.keys())
['c', 'd', 'b', 'a']
>>> list(chain.values())
[13, 14, 12, 11]
>>> chain.maps
[{'a': 11, 'b': 12}, {'c': 13, 'd': 14}]
>>> mylist = [1,2,3,4,5]
>>> all(mylist)
True
>>> mylist = [1,2,3,4,5,False]
>>> all(mylist)
False
>>> any(mylist)
True
>>> mylist = [False,False]
>>> any(mylist)
False

"""