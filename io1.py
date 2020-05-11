'''def printInfo1(name,age,isVoter,a,b):
    print("This is my info ", name,age,isVoter)
    print("Hello, this is ", name,", my age is ", age,"can i vote? ", isVoter)
    print(f"Hello, this is {a/b} my age is {age}, can i vote? {isVoter}")

printInfo1('Rajesh',25,True,10,2)


def printInfo2(name,age,isVoter):
    print("Hello, this is {0} my age is {1}, can i vote? {2}".format(name,age,isVoter))

printInfo2('Rajesh',25,True)


def printInfo3(stdinfo):
    #print("{0}".format(stdinfo))
    print("First: {0[11]:d}; Second: {0[12]}; Third: {0[13]}".format(stdinfo))
    #print("{0.11}".format(**stdinfo))

stdinfo = {11:100,12:'suraj',13:'tej'}

printInfo3(stdinfo)
'''

for x in range(11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))