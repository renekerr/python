from turtle import Turtle, Screen
from random import randint


t = Turtle()
scr = Screen()

t.color('black')
t.shape('arrow')
t.shapesize(0.2)
t.speed('fastest')
t.pensize(1)

scr.colormode()
scr.colormode(255)

degrees = 360
number_sides = 4


def draw_shape(n_sides):
    """Draw shape based on number of sides"""
    for _ in range(n_sides):
        angle = degrees / n_sides
        t.forward(50)
        t.left(angle)


def random_color():
    """Add random color to each line"""
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    t.pencolor(r, g, b)


# Multicolored poly shaped figure
while number_sides <= 10:
    random_color()
    draw_shape(n_sides=number_sides)
    number_sides += 1

scr.exitonclick()
