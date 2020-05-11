print("before error")

try:
    raise ValueError('arg1','arg2')
except ValueError as err:
    print(type(err))
    print(err.args)
    print(err)

print("after error")