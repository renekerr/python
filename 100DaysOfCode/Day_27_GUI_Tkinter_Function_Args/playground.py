# Function to add any number of positional arguments
def add(*args):
    """Adds an arbitrary number of numeric arguments and prints the result."""
    s = 0
    for i in args:
        s += i
    print(s)  # Output the sum of all arguments


# Calling add() with several arguments to demonstrate *args functionality
add(3, 5, 6, 6, 7, 3)


# Function to perform calculations using keyword arguments
def calculate(n, **kwargs):
    """Modifies n by adding and multiplying with keyword argument values."""
    n += kwargs['add']  # Add the value of 'add' in kwargs to n
    n *= kwargs['multiply']  # Multiply n by the value of 'multiply' in kwargs
    print(n)  # Output the final result after calculations


# Calling calculate() with n and two keyword arguments
calculate(2, add=3, multiply=5)


# Car class that accepts optional attributes using **kwargs
class Car:
    """Represents a car with optional attributes: make, model, year, and color."""

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')  # Car make
        self.model = kwargs.get('model')  # Car model
        self.year = kwargs.get('year')  # Car manufacturing year
        self.color = kwargs.get('color')  # Car color


# Creating a Car object with specified attributes and printing them
new_car = Car(make='Kia', model='Sportage HEV', year=2022, color='Yucca')

# Output the details of the car instance
print(f"Make & Model: {new_car.make}, {new_car.model}")
print(f"Year: {new_car.year}")
print(f"Color: {new_car.color}")
