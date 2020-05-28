#4 UserList - list with extra methods for customization
from collections import UserList, UserString, Counter
'''
mylist = [1,2,"rajesh",False,(1,2,3)]
#append, extend, remove,copy,del,pop

print(mylist)

myuserList1 = UserList()
print(myuserList1)

myuserList2 = UserList(mylist)
print(myuserList2.pop())

class MySpecialList(UserList):
    def pop(self, k=None):
        raise RuntimeError("Deletion is not allowed in MySpecialList")

myuserList3 = MySpecialList(mylist)
print(myuserList3)
print(myuserList3.pop())

#4 UserString - string with extra methods for customization
name1 = "123"
name2 = "rajesh"
#reverse,copy,append(no append function in string so we can user user string)

>>> name = "rajes"
>>> name.append('h')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'


class MySpecialString(UserString):
    def append(self,s):
        self.data += s

name = MySpecialString("rajes")
print(name)
name.append('h')
print(name)
'''
#5 counter - special data set for large amount of data processing
# works on hashable object
#mycounter2 = Counter("rajesh singh")
#{'s': 2, 'h': 2, 'r': 1, 'a': 1, 'j': 1, 'e': 1, ' ': 1, 'i': 1, 'n': 1, 'g': 1}
# elements method
counter = 0
while counter <=5:
    print(counter)
    counter = counter+1

mycounter1 = Counter()
print(mycounter1)

for i in mycounter1.elements():
    print(i)

mycounter2 = Counter("rajesh singh")
print(mycounter2)

for i in mycounter2.elements():
    print(i)




