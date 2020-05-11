#Multilevel
class A:
    def info(self):
        print("From class A")

class B(A):
    def info(self):
        print("From class B")

class C(B):
    def info(self):
        print("From class C")

obj = C()
obj.info()