# Day 22- Building Pong Game.

# TODO: Create a screen (DONE)
# TODO: Create and move a paddle (DONE)
# TODO: Create another paddle (DONE)
# TODO: Create a ball and make it move (DONE)
# TODO: Detect collision with wall and bounce (DONE)
# TODO: Detect collision with paddle (DONE)
# TODO: Detect when paddle misses (DONE)
# TODO: Keep a score (DONE)

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from divisoryline import DivLine
from time import sleep

seconds = 0.1

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong |.|', )
screen.tracer(0)

# Create paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Create a ball
ball = Ball()

# Create a scoreboard
scoreboard = Scoreboard()

# Create a divisor line
divisor_line = DivLine()

# Key listening. Paddles movements.
screen.listen()
screen.onkey(fun=right_paddle.go_up, key='Up')
screen.onkey(fun=right_paddle.go_down, key='Down')
screen.onkey(fun=left_paddle.go_up, key='w')
screen.onkey(fun=left_paddle.go_down, key='s')

# Game loop control and screen update
# Pause briefly to control ball's movement speed
game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)

    # Move the ball according to its current direction
    ball.move()

    # Check if the ball hits the top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check if the ball hits a paddle and bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Check if the right paddle misses the ball and update score
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Check if the left paddle misses the ball and update score
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

# Exit the game when the screen is clicked
screen.exitonclick()
