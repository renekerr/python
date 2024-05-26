from turtle import Turtle, Screen
from random import randint, choice


t = Turtle()
t.color('black')
t.shape('circle')
t.shapesize(0.2)
t.speed('fast')
t.pensize(40)

screen = Screen()
screen.colormode()
screen.colormode(255)

directions = [0, 90, 180, 270]


def random_walk(turns, steps):
    """Generate a random walk pattern with specified number of turns and steps size."""
    for _ in range(turns):
        random_color()
        t.forward(steps)
        t.setheading(choice(directions))


def random_color():
    """Add random color to each line"""
    r, g, b = randint(0,  255), randint(0, 255), randint(0, 255)
    t.pencolor(r, g, b)


random_walk(turns=1000, steps=50)

screen.exitonclick()