#collection - specialized container datatypes for alternative to genral purpose type list,set,dict,tuple
#for better performance

'''
1. namedtuple
2.deque
3.chainmap
4.counter
5.ordered dict
6.default dict
7.user dict
8. user list
9. user string
'''
'''
#1. Default dictionary - special dict with default value if we try to access a non existing key
from _collections import defaultdict

def def_value():
    return 0

my_default_dict = defaultdict(def_value)
my_default_dict['a']=11
my_default_dict['b']=12
print(my_default_dict)
print(my_default_dict['a'])
print(my_default_dict['b'])
print(my_default_dict['c'])


mydict = {'a':11,'b':12}
print(mydict['a'])
print(mydict['b'])
#print(mydict['c'])


#2. User dict - user defined with extra power
from collections import UserDict

mydict1 = {'a':11,'b':12,'c':13}
print(mydict1)
print(mydict1.pop('b'))
print(mydict1)

class MySpecialDict(UserDict):
    def pop(self, k= None):
        raise RuntimeError("Deletion is not allowed in MySpecialDict")

try:
    mydict2 = MySpecialDict({'a':11,'b':12,'c':13})
except RuntimeError as e:
    print(e)

print(mydict2)
try:
    print(mydict2.pop(['c']))
except RuntimeError as e:
    print(e)
print(mydict2)

'''
#3 OrderedDict remembers who came first(insertion oreder) but in python 3 even ordinary dict remembers
from collections import OrderedDict

'''
mydict1 = {'a':17,'b':10,'c':3,'d':102}
print(mydict1)

for i,j in mydict1.items():
    print(i,j)
'''
mydict2 = {}
mydict2['a'] = 17
mydict2['b'] = 10
mydict2['c'] = 5
print(mydict2)

for i,j in mydict2.items():
    print(i,j)

mydict3 = OrderedDict()
mydict3['a'] = 17
mydict3['b'] = 10
mydict3['c'] = 5
print(mydict3)

for i,j in mydict3.items():
    print(i,j)