from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        """Initialize the Food object.

        This sets up the attributes of the food turtle, including its appearance
        and initial position on the screen.
        """
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = randint(-270, 270)
        random_y = randint(-270, 270)
        self.goto(random_x, random_y)
