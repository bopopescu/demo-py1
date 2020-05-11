class Person:
    def __init__(self,name,acard):
        self.name = name
        self.acard = acard

    def myInfo(self):
        print("This is my info ",self.name,self.acard)


class Employee(Person):
    def __init__(self,name,acard,salary):
        super().__init__(name,acard)
        self.salary = salary

    def myInfo(self):
        super().myInfo()
        print("Salary is ",self.salary)

class Student(Person):
    def __init__(self,name, acard,marks):
        super().__init__(name, acard)
        self.marks = marks

    def myInfo(self):
        super().myInfo()
        print("Marks are ",self.marks)

p1 = Person("Tom",567)
e1 = Employee("Raj",123,5000)
s1 = Student("Suraj",234,96)
p1.myInfo()
e1.myInfo()
s1.myInfo()

