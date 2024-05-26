from turtle import Turtle

STARTING_POSITION = [(0, 0), (-21, 0), (-42, 0)]
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
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[1:]

    def create_snake(self):  # create_snake() and add_segment() are going to create a snake
        """ Create a snake in given position"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """ Create a snake in given position"""
        snk = Turtle(shape='square')
        snk.color('white')
        snk.penup()
        snk.goto(position)
        self.snake_segments.append(snk)

    def extend(self):
        """ Add a snake segment at the end every time snake eats some food"""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        """
        Move the snake forward.

        Updates each segment's position in reverse order.
        Moves the head segment forward by 20 units.
        """
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()  # Get previous segment's x-coordinate
            new_y = self.snake_segments[seg_num - 1].ycor()  # Get previous segment's y-coordinate
            self.snake_segments[seg_num].goto(new_x, new_y)  # Move current segment to the new position

        # Move the head segment forward by 20 units
        self.head.forward(MOVE_DISTANCE)

        """
        # Approach
        Move the third segment to the position of the second.
        Move the second segment to the position of the first.
        Finally, move the first segment either to the right or to the left. 
        """

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
