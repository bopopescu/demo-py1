mylist = [1,2,3,4,5]

itr = iter(mylist)
print(itr)
print(itr.__next__())

mylist1  = [2,3,4,5]
itr = iter(mylist1)
itrtuple = tuple(itr)
print(itrtuple)
#(2, 3, 4, 5) run again, it will be exhusted.

#built in iterators - list,dict,tuples
'''
for i in mylist:
    print(i**2)

name = "rajesh"

for i in name:
    print(i)

name = "rajesh"
itr = iter(name)
while True:
    try:
        item = next(itr)
        print(item)
    except StopIteration:
        print("Exhusted.")
        break
'''
