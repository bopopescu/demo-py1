'''
def add(a,b,*c):
    r = 0
    for i in c:
        r = r+i
    return a+b+r

result = add(10,15,16,15,56)
print(result)


def add(a,b=5):
    return a+b

result = add(10)
print(result)


def add(a,b=5,*c,**d):
    print(a,b,c,d)

add(10,2,4,5,6,7,e=56,f=45)
'''

def add(a,b=5,*args,**kwargs):
    print(a,b,args,kwargs)

#add(10,2,4,5,6,7,e=56,f=45)
add(10,2,4,5,6,7,6,7,8,e=56,f=45,t=67)
#add(10,2,4,5,6,7,b=34,e=56,f=45)
