from turtle import Turtle
from random import choice

ALIGNMENT = 'center'
FONT = ('Verdana', 10, 'normal')

GRAPHIC_SCALE = 20
INITIAL_SEGMENT_LENGTH = 4
RATIO = 0.5
OUTLINE = 5
MOVE_DISTANCE = GRAPHIC_SCALE * RATIO

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

STARTING_DIRECTION = (0, 90, 180, 270)


class Snake:
    """A class representing a snake object in a game."""

    def __init__(self):
        """Initialize a snake with default parameters."""

        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[2:]
        self.head.setheading(choice(STARTING_DIRECTION))

    def create_snake(self):
        """Create the initial segments of the snake."""
        for _ in range(INITIAL_SEGMENT_LENGTH):
            self.add_segment()

    def add_segment(self, position=(0, 0)):
        """Add a new segment to the snake."""
        new_segment = Turtle(shape='square')
        new_segment.color('grey')
        new_segment.shapesize(stretch_wid=RATIO, stretch_len=RATIO, outline=OUTLINE)
        new_segment.penup()
        new_segment.speed('fastest')
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def reset(self):
        """Reset snake to starting position"""

        # Send off-screen snake firstly
        for seg in self.snake_segments:
            seg.goto(1000, 1000)

        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.setheading(choice(STARTING_DIRECTION))

    def extend(self):
        """Extend the snake by adding a new segment."""
        self.add_segment(position=self.snake_segments[-1].position())

    def move(self):
        """Move the snake forward by one segment length."""
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    """
         # Approach
         Move the third segment to the position of the second.
         Move the second segment to the position of the first.
         Finally, move the first segment either to the right or to the left. 
     """

    def right(self):
        """Change the snake's heading to the right (east) if not already heading left (west)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """Change the snake's heading upward (north) if not already heading downward (south)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """Change the snake's heading to the left (west) if not already heading right (east)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Change the snake's heading downward (south) if not already heading upward (north)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
