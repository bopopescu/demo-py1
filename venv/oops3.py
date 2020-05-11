class Person:

    def __init__(self,name,acard):
        self.name = name
        self.acard = acard
        self.salary = 0

    # def myInfo(self):
    #     print("This is my info ",self.name,self.acard)

    def myInfo(self,salary=10):
        print("This is my info ",self.name,self.acard,self.salary)


p1 = Person("Raj",234)
p1.myInfo(2000)
p1.myInfo()
