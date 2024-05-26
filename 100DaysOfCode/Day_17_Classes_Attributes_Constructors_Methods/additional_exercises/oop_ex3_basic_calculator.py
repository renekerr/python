# Create a calculator class.
# Include methods for basic arithmetic operations.

class Calculator:
    """
    A simple calculator class for basic arithmetic operations.
    """

    def add(self, value1, value2):
        """
        Adds two numbers and returns the result.
        """
        return value1 + value2

    def subtract(self, value1, value2):
        """
        Subtracts the second number from the first and returns the result.
        """
        return value1 - value2

    def multiply(self, value1, value2):
        """
        Multiplies two numbers and returns the result.
        """
        return value1 * value2

    def divide(self, value1, value2):
        """
        Divides the first number by the second and returns the result.
        If the second number is zero, returns an error message.
        """
        if value2 == 0:
            return 'Division by zero is not allowed.'
        return value1 / value2


calc = Calculator()


print("Welcome to the Simple Calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")
result = 0
ops = {
    '+': calc.add(num1, num2),
    '-': calc.subtract(num1, num2),
    '*': calc.multiply(num1, num2),
    '/': calc.divide(num1, num2),
}


if operation in ops:
    result = ops[operation]
print(f"{num1} {operation} {num2} = {result}")

