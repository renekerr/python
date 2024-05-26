from turtle import Turtle


class DivLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.right(90)
        self.pendown()
        self.goto(0, -280)
