import module1

#can we give same name as of global variables in module in our python file?
# because each module has its own private symbol table.
a =20
#print("from module util",a)
#print(" accessing module value ",module1.a)

print("module name is ",module1.__name__)

module1.addition(10,20)
module1.subtraction(20,10)