from turtle import Turtle, Screen
from random import choice

color_palette = [(201, 165, 111), (39, 98, 131), (124, 84, 55),
                 (128, 163, 187), (233, 206, 110), (173, 148, 45), (196, 75, 110), (139, 56, 74), (222, 126, 144),
                 (115, 40, 71),
                 (56, 46, 44), (87, 168, 117), (219, 69, 55), (101, 197, 189), (245, 160, 169), (43, 156, 204),
                 (68, 107, 76),
                 (1, 61, 85), (210, 184, 181), (85, 51, 46), (63, 58, 61), (156, 210, 202), (160, 205, 213),
                 (122, 124, 154),
                 (188, 188, 202), (19, 82, 98), (69, 68, 57), (65, 57, 94)]


def draw_random_dots(pos_x, pos_y):
    """ Draws a line of random colored dots at the specified position. """
    for _ in range(dots_per_line):
        color = choice(color_palette)
        pos_x += 50
        t.dot(dot_radius, color)
        t.goto(pos_x, pos_y)


x = -150
y = -150
dots_per_line = 10
dot_radius = 30
total_rows = 10

# Turtle class
t = Turtle()
t.penup()
t.setx(x)
t.sety(y)
t.speed('fast')
t.hideturtle()

# Screen class
screen = Screen()
screen.colormode()
screen.colormode(255)

while total_rows > 0:
    draw_random_dots(pos_x=x, pos_y=y)
    x = -150
    y -= -50
    t.setx(x)
    t.sety(y)
    total_rows -= 1


screen.exitonclick()
