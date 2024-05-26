from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier New', 50, 'normal')


class Scoreboard(Turtle):
    """A class representing the scoreboard in the Pong game."""

    def __init__(self):
        """Initialize a scoreboard object."""
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display."""
        self.clear()
        self.goto(100, 200)
        self.write(f'{self.right_score}', align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(f'{self.left_score}', align=ALIGNMENT, font=FONT)

    def right_point(self):
        """Update right player's score."""
        self.right_score += 1  # Increment right player's score
        self.update_scoreboard()  # Update scoreboard display

    def left_point(self):
        """Update left player's score."""
        self.left_score += 1  # Increment left player's score
        self.update_scoreboard()  # Update scoreboard display
