# TODO: Create a screen (DONE)
# TODO: Create a snake body (DONE)
# TODO: Move the snake (DONE)
# TODO: Create snake food (DONE)
# TODO: Detect collision with food (DONE)
# TODO: Create a scoreboard (DONE)
# TODO: Detect collision with wall (DONE)
# TODO: Detect collision with tail (DONE)

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

seconds = 0.09

# Set up the game screen with specified dimensions and appearance
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Snake Game 🐍🐍🐍')
screen.tracer(0)

"""
Using tracer(0) and update() together allows developers to achieve smoother animations, 
reduce rendering overhead, and maintain control over the timing and frequency of screen updates, 
ultimately leading to a more polished and efficient graphical experience in Turtle-based projects.
"""


# Create a snake object for gameplay
snake = Snake()

# Create a food object for the snake to consume
food = Food()

# Create a scoreboard to track and display game statistics
scoreboard = Scoreboard()

# Enable listening for keyboard input to control snake movement
screen.listen()
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.down, key='Down')

# Main game loop
game_is_on = True
while game_is_on:
    # Update the screen to reflect the current game state
    screen.update()

    # Pause briefly to control the game speed
    sleep(seconds)

    # Move the snake forward by updating its position based on current direction
    snake.move()

    # Check if the snake has collided with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Check for collision with game boundaries (walls)
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 275 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over_hit_wall()

    # Check for collision with the snake's own tail
    for segment in snake.tail:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over_hit_tail()

# Cleanly exit the game when the user clicks on the screen
screen.exitonclick()
