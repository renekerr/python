from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_LENGTH = 0.5
OUTLINE = 3


class Paddle(Turtle):
    """A class representing a paddle in the Pong game."""

    def __init__(self, position):
        """Initialize a paddle object. Args: position (tuple): The initial position of the paddle."""
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH, outline=OUTLINE)
        self.goto(position)

    def go_up(self):
        """Move the paddle up."""
        if self.ycor() < 240:  # Check if paddle is not at top boundary
            new_y = self.ycor() + 20  # Calculate new y-coordinate
            self.goto(self.xcor(), new_y)  # Move paddle to new position

    def go_down(self):
        """Move the paddle down."""
        if self.ycor() > -240:  # Check if paddle is not at bottom boundary
            new_y = self.ycor() - 20  # Calculate new y-coordinate
            self.goto(self.xcor(), new_y)  # Move paddle to new position
