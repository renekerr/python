# Tuples (items in a tuple cannot be changed, they are IMMUTABLE)
from turtle import Turtle, Screen
from random import randint, choice

t = Turtle()
t.color('black')
t.shape('circle')
t.shapesize(0.2)
t.speed('fastest')
t.pensize(1)

screen = Screen()
screen.colormode()
screen.colormode(255)

# Example of a tuple
my_tuple = (1, 10, 100)
print(type(my_tuple))   # <class 'tuple'>

print(my_tuple[1])  # 10

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 11

directions = [0, 90, 180, 270]


def random_color():
    """Add random color to each line using a tuple"""
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


for _ in range(1000000):
    t.forward(20)
    t.color(random_color())
    t.setheading(choice(directions))

screen. exitonclick()
