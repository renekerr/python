# Day 21- Building Snake Game II. Class Inheritance and slicing.

# Day 1
# TODO: Create a snake body (DONE)
# TODO: Move the snake  (DONE)

# Day 2
# TODO: Create snake food (DONE)
# TODO: Detect collision with food (DONE)
# TODO: Create a scoreboard (DONE)
# TODO: Detect collision with wall (DONE)
# TODO: Extend snake when it eats food (DONE)
# TODO: Detect collision with tail (DONE)

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

# Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

# Create a snake and position it
snake = Snake()

# Create snake food
food = Food()

# Create a scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

# Move the snake
game_on = True
while game_on:
    screen.update()  # Update the screen
    sleep(0.1)  # Pause for n seconds (controls snake speed)

    # Move the snake forward
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # Checks distance between to snake head to food
        food.refresh()
        snake.extend()  # Extend snake by one segment
        scoreboard.increase_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.tail:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

# Exit the game when the user clicks anywhere on the screen
screen.exitonclick()
