from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana', 10, 'normal')


class Scoreboard(Turtle):
    """A class representing a scoreboard for displaying the score in a turtle game."""

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highest_score.txt") as data:
            self.high_score = int(data.read())  # reading from file

        self.color('grey')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard display."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.clear()
        self.goto(x=170, y=275)
        self.write(arg=f'HIGHEST SCORE: {self.high_score} | SCORE: {self.score}', align=ALIGNMENT, font=FONT)
        self.info()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def info(self):
        self.goto(x=-215, y=275)
        self.write(arg=f"'ESC' TO EXIT GAME", align=ALIGNMENT, font=FONT)
