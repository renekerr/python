from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
ALIGNMENT = 'center'
FONT = ("Courier", 12, "normal")


class Player(Turtle):
    """Manages the creation of a player"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.go_to_start_position()

    def go_up(self):
        """Move player forward"""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """Move player forward"""
        self.backward(MOVE_DISTANCE)

    def collision_detected(self):
        """Displays a text message when player collides with a car"""
        self.goto(-0, 250)
        self.write('Collision with car detected. Game over.', align=ALIGNMENT, font=FONT)

    def reach_top_edge(self):
        """Confirms when player has reached top edge of the screen"""
        if self.ycor() > FINISH_LINE_Y:
            return True

    def go_to_start_position(self):
        """Reset player to start position"""
        self.goto(STARTING_POSITION)
