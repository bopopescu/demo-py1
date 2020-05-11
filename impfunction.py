#map,filter,reduce
from functools import reduce

def even(x):
    if x%2==0:
        return x

def square(x):
    return x**2

def add(x,y):
    return x+y

result1 = map(square,range(5))
print(list(result1))

result2 = filter(even,range(5))
print(list(result2))

#[0,1,2,3,4] add(0,1) => 1, add(1,2) => 3, add(3,3) => 6, add(6,4) => result is 10
result3 = reduce(add, range(5))
print(result3)