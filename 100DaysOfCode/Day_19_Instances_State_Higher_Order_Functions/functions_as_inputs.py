# Higher Order Functions
# Functions as inputs
"""
def function_a(something):
    # Do this with something
    # Then do this
    # Finally do this

def function_b():
    # Do this

function_a(function_b) # Notice that when we pass the name we do not add the (), just the name
"""


# Example
def add(value1, value2):
    return value1 + value2


def subtract(value1, value2):
    return value1 - value2


def multiply(value1, value2):
    return value1 * value2


def divide(value1, value2):
    if value2 == 0:
        return 'Division by zero is not allowed.'
    return value1 / value2


# This calculator function is an example of a Higher Order Function
# This means that it can work with other functions
def calculator(value1, value2, func):
    return func(value1, value2)


result = calculator(value1=2, value2=3, func=multiply)  # Pass the function without ()
print(result)
