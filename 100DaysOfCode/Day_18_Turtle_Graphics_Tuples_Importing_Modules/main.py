# Day 18- Turtle Graphics. Tuples. Importing_Modules

"""
# Aliasing a module
import heroes as h


# Generating hero name
print(h.gen())
"""
from turtle import Turtle, Screen


tommy = Turtle()
screen = Screen()


# Modifying object
tommy.shape('circle')
tommy.shapesize(0.3)
tommy.color('black')

# Drawing a square
for _ in range(4):
    tommy.forward(100)
    tommy.left(90)


screen.exitonclick()
