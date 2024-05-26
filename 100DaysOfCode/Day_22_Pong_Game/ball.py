from turtle import Turtle


class Ball(Turtle):
    """A class representing a ball in the Pong game."""

    def __init__(self):
        """Initialize a ball object."""
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.7)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball."""
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate
        self.goto(new_x, new_y)  # Move ball to new position

    def bounce_y(self):
        """Change vertical movement direction."""
        self.y_move *= -1  # Reverse vertical movement direction

    def bounce_x(self):
        """Change horizontal movement direction and reduce speed."""
        self.x_move *= -1  # Reverse horizontal movement direction
        self.move_speed *= 0.9  # Reduce movement speed

    def reset_position(self):
        """Reset the ball's position and movement speed."""
        self.goto(0, 0)  # Move ball to center
        self.move_speed = 0.1  # Reset movement speed
        self.bounce_x()  # Reverse horizontal movement direction
