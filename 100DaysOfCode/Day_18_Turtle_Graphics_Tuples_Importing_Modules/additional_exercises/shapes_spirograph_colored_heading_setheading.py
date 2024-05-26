# Drawing a spirograph randomly colored

from turtle import Turtle, Screen
from random import randint

t = Turtle()
t.color('black')
t.shape('arrow')
t.shapesize(0.2)
t.speed('fastest')
t.pensize(1)

screen = Screen()
screen.colormode()
screen.colormode(255)


t.home()
pos = t.position()


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


def random_color():
    """Add random color to each line"""
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    color = (r, g, b)
    return color


draw_spirograph(5)


screen.exitonclick()
