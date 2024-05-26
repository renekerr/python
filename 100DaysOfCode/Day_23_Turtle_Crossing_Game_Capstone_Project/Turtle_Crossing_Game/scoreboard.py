from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    """Tracks and displays the game level on the screen."""

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(240, 270)
        self.update_level()

    def update_level(self):
        """Clears the previous level text and writes the new level."""
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        """Increases the level by 1 and updates the scoreboard."""
        self.level += 1
        self.update_level()
