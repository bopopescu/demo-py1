mylist = ["raj","rajesh","john","tom","suraj"]

itr = iter(mylist)
print(tuple(itr))

#custm iterator
#__iter__(), __next__

class MyIter:
    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):
        self.i = 3
        return self

    def __next__(self):
         i  = self.i

         if i > self.limit:
             raise StopIteration
         self.i = i + 1;
         return i

itrobj = MyIter(5)
for i in itrobj:
    print(i)

#for i in mylist:

#wap to print reverse of string using iterator
#rajesh => hsejar




