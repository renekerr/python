from turtle import Turtle
from random import randint


class Food(Turtle):
    """A class representing food in a turtle game."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5)
        self.color('grey')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Move the food to a random position within the screen boundaries."""
        random_x = randint(a=-280, b=270)
        random_y = randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)

