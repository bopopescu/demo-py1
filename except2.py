import sys

print("before error")

try:
    f= open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print("value of i is ",i/0)
except FileNotFoundError as err:
    print("File not found occured ",err.filename)
except ValueError as verr:
    print("Value error occured " ,verr.args)
except:
    print("Unexpected error occurred.")

print("after error")