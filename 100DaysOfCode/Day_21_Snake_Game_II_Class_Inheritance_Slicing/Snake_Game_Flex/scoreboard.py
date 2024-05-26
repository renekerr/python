from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier New', 18, 'normal')


class Scoreboard(Turtle):
    """A class representing a scoreboard for displaying the score in a turtle game."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('grey')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard display."""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.write(arg=f'SCORE: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over_hit_wall(self):
        """Handle game over when hitting a wall."""
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(arg="COLLISION WITH WALL DETECTED", align=ALIGNMENT, font=FONT)

    def game_over_hit_tail(self):
        """Handle game over when colliding with the tail."""
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(arg="COLLISION WITH TAIL DETECTED", align=ALIGNMENT, font=FONT)

