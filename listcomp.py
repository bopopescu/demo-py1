square1 = []

for i in range(1,10):
    if i%2 == 0:
        square1.append(i**2)

print("square1",square1)

#consise way of creating a list
# [] bracket, expression - i**2,followed by for clause, more for or if clause
square2 = [i**2 for i in range(1,10)]
print("square2",square2)

square3 = [i**2 for i in range(1,10) if i%2==0 ]
print("square3",square3)

square4 = [(i,i**2) for i in range(1,10) if i%2==0 ]
print("square4",square4)

mylistcomp = [(x,y) for x in [1,2,3] for y in [4,5,6]]
print(mylistcomp)

def add(x,y):
    return x+y

addcomp = [add(i,j) for i in [1,2,3] for j in [4,5,6] ]
print(addcomp)

#flattening the list from [[5, 6, 7], [6, 7, 8], [7, 8, 9]] to [5, 6, 7, 6, 7, 8, 7, 8, 9]
mylist = [[5, 6, 7], [6, 7, 8], [7, 8, 9]]
mycompflat = [i for x in mylist for i in x]
print(mycompflat)