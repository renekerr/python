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


def draw_spirograph(radius_value, extent_value, steps_value, theta):
    """Draw a spirograph based on given values like radius, extent, steps and angle"""
    number_of_circles = int(360 / theta)
    for _ in range(number_of_circles):
        random_color()
        t.circle(radius_value, extent_value, steps_value)
        t.left(theta)


def random_color():
    """Add random color to each line"""
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    t.pencolor(r, g, b)


draw_spirograph(radius_value=50, extent_value=None, steps_value=None, theta=5)


screen.exitonclick()
