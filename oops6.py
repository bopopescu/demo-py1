#Multiple
class A1:
    def info(self):
        print("From class A")

class A2:
    def info(self):
        print("From class B")

#MRO method resolution order - current class, left to right
class C(A2,A1):
    def info(self):
        super().info()
        print("From class C")

obj = C()
obj.info()