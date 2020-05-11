def add(x,y):
    return x+y

addcomp1 = [add(i,j) for i in [1,2,3] for j in [4,5,6] ]
print(addcomp1)

addlambda = lambda x,y:x+y
print(addlambda(10,15))

addcomp2 = [(lambda x,y:x+y)(x,y) for x in [1,2,3] for y in [4,5,6] ]
print(addcomp2)
