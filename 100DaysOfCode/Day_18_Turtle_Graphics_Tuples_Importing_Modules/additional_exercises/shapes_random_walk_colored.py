from turtle import Turtle, Screen
from random import randint


t = Turtle()
t.color('black')
t.shape('circle')
t.shapesize(0.2)
t.speed('fast')
t.pensize(4)

screen = Screen()
screen.colormode()
screen.colormode(255)


def random_walk(turns, steps):
    """Generate a random walk pattern with specified number of turns and steps size."""
    for _ in range(turns):
        random_color()
        n = randint(0, 1)
        t.forward(steps)
        if n == 0:
            t.right(90)
        else:
            t.left(90)


def random_color():
    """Add random color to each line"""
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    t.pencolor(r, g, b)


random_walk(turns=500, steps=50)

screen.exitonclick()
