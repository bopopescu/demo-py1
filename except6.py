a= int(input("Please enter value of a "))
b= int(input("Please enter value of b "))

def division(a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError:
        print("Make sure you do not divide by zero.")
    finally:
        print("Always gets excuted.")
    return result
result = division(a,b)

print(result)
print("after error")