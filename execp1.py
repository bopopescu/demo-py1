print("before error")
#a= 10
#b= 5
a= int(input("Please enter value of a "))
b= int(input("Please enter value of b "))

def division(a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError:
        print("Make sure you do not divide by zero.")
    return result
result = division(a,b)

print(result)
print("after error")