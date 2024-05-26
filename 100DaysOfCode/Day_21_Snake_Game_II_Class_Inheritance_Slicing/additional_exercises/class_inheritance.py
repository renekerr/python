# Example of class inheritance

class Animal:
    """Represents an animal with 2 eyes that can breathe."""

    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        """Simulates breathing by inhaling and exhaling."""
        print('- inhale and exhale')


class Fish(Animal):
    """Represents a fish, inheriting from Animal, adapted to aquatic life."""

    def __init__(self):
        super().__init__()
        self.colored = True

    def breathe(self):
        """Overrides Animal breathe method for underwater breathing."""
        super().breathe()
        print('- do this underwater')

    def swim(self):
        """Simulates swimming in water."""
        print('- swim, moving in the water')


nemo = Fish()
print('Nemo can:')
nemo.breathe()
nemo.swim()
print(f'Nemo has {nemo.number_of_eyes} eyes.')
print(f'Nemo is a colored fish: {nemo.colored}')

"""
This code demonstrates class inheritance in Python. 
It defines an Animal class with a constructor that initializes the number_of_eyes attribute and a method breathe() that 
simulates breathing. The Fish class inherits from Animal and overrides the breathe() method to add underwater breathing 
behavior and introduces a new method swim().

When executed, it creates an instance nemo of the Fish class and demonstrates its capabilities by calling breathe() and 
swim() methods, displaying the respective behaviors of underwater breathing and swimming.
"""
