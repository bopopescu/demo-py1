#6 namedtuple - key and index, get attribute
from collections import namedtuple
mytup = (101,11,2,33)
# 2,11,33,101
print(mytup[2])
mytup = (101,11,2,33)
print(tuple(sorted(mytup)))
#copy, reverse, max ,min,len,

Emp = namedtuple('Emp',['eid','ename','salary'])

emp1 = Emp(101,'raj',5000)
print(emp1)
print(emp1[0]) #access by index
print(emp1.ename) #access by key
print(getattr(emp1,'salary')) #accessing using get attribute

