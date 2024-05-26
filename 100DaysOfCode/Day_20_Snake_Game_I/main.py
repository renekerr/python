# Day 20- Building Snake Game

# Day 1
# TODO: Create a snake body (DONE)
# TODO: Move the snake  (DONE)
# TODO: Create snake food

# Day 2
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Screen
from snake import Snake
from time import sleep

# Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍', )
screen.tracer(0)

# Create a snake and position it
snake = Snake()

screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

# Move the snake
game_on = True
while game_on:
    screen.update()  # Update the screen
    sleep(0.1)  # Pause for 1 second (controls snake speed)

    # Move the snake forward
    snake.move()

# Exit the game when the user clicks anywhere on the screen
screen.exitonclick()

"""
# Approach
Move the third segment to the position of the second.
Move the second segment to the position of the first.
Finally, move the first segment either to the right or to the left. 
"""
