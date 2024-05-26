from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        """Initialize the Scoreboard object.

        This sets up the attributes of the food turtle, including its appearance
        and initial position on the screen.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.color('white')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'SCORE: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)
