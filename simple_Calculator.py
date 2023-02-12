class Calculator:
    a = int(),float(),complex()
    b = int(),float(),complex()

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        print(a / b)


x = Calculator()
x.add(1, 1)
x.divide(2,4)
x.subtract(2,4)
x.multiply(2,4)
