class MyError(Exception):
    def __init__(self,vlaue):
        self.value = vlaue

    def __str__(self):
        return (repr(self.value))

print("before error")

try:
    raise MyError(10*2)
except MyError as err:
    print(type(err))
    print(err.args)
    print(err)

print("after error")