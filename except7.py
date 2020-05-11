a= int(input("Please enter value of a "))
b= int(input("Please enter value of b "))

def division(a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError:
        print("Make sure you do not divide by zero.")
    else:
        print("Additional code.")
    return result
result = division(a,b)

print(result)
print("after error")