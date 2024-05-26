from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """Represents a snake game."""

    def __init__(self):
        """
        Initialize the Snake class.

        Creates a snake with 3 segments, positioned horizontally.
        """
        self.snk_segments = []
        self.create_snake()
        self.head = self.snk_segments[0]

    def create_snake(self):
        """Create a snake in given position"""
        for position in STARTING_POSITION:
            snk = Turtle(shape='square')
            snk.color('white')
            snk.penup()
            snk.goto(position)
            self.snk_segments.append(snk)

    def move(self):
        """
        Move the snake forward.

        Updates each segment's position in reverse order.
        Moves the head segment forward by 20 units.
        """
        for seg_num in range(len(self.snk_segments) - 1, 0, -1):
            new_x = self.snk_segments[seg_num - 1].xcor()  # Get previous segment's x-coordinate
            new_y = self.snk_segments[seg_num - 1].ycor()  # Get previous segment's y-coordinate
            self.snk_segments[seg_num].goto(new_x, new_y)  # Move current segment to the new position

        # Move the head segment forward by 20 units
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        """
        Change the snake's direction to the right (east).
        The snake cannot turn directly opposite its current direction.
        This prevents the snake from immediately reversing direction.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """
        Change the snake's direction upwards (north).
        The snake cannot turn directly opposite its current direction.
        This prevents the snake from immediately reversing direction.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """
        Change the snake's direction to the left (west).
        The snake cannot turn directly opposite its current direction.
        This prevents the snake from immediately reversing direction.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """
        Change the snake's direction downwards (south).
        The snake cannot turn directly opposite its current direction.
        This prevents the snake from immediately reversing direction.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
