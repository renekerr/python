from turtle import Turtle, Screen
from time import sleep
from random import choice, randint

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
rand_y1 = randint(-260, 260)
rand_y2 = randint(-260, 260)
rand_y3 = randint(-260, 260)

screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

car1 = Turtle(shape='square')
car1.penup()
car1.setheading(180)
car1.color(choice(colors))
car1.shapesize(stretch_wid=1, stretch_len=2, outline=5)
car1.goto(265, rand_y1)

car2 = Turtle(shape='square')
car2.penup()
car2.setheading(180)
car2.color(choice(colors))
car2.shapesize(stretch_wid=1, stretch_len=2, outline=5)
car2.goto(265, rand_y2)

car3 = Turtle(shape='square')
car3.penup()
car3.setheading(180)
car3.color(choice(colors))
car3.shapesize(stretch_wid=1, stretch_len=2, outline=5)
car3.goto(265, rand_y3)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    car1.forward(5)
    car2.forward(5)
    car3.forward(5)

screen.exitonclick()
