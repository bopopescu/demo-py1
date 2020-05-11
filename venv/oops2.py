class Calculator:
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b

    def addition(self):
        return self.val1 + self.val2

    def subtraction(self):
        return self.val1 - self.val2

    def multiplication(self):
        return self.val1 * self.val2

    def division(self):
        return self.val1 / self.val2


calc1 = Calculator(25,5)
print(calc1.addition())
print(calc1.subtraction())
print(calc1.multiplication())
print(calc1.division())