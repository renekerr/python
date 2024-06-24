from turtle import Turtle
from random import randint


class Food(Turtle):
    """A class representing food in a turtle game."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.3)
        self.color('black')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Move the food to a random position within the screen boundaries."""
        random_x = randint(a=-280, b=250)
        random_y = randint(a=-260, b=260)
        self.goto(x=random_x, y=random_y)
