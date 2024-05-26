# TODO Create the turtle or player (DONE)
# TODO Move the turtle (DONE)
# TODO Create and move the cars (DONE)
# TODO Detect collision with car (DONE)
# TODO Detect when turtle reach the other side (DONE)
# TODO Create a scoreboard (DONE)

# Imports
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

from time import sleep

seconds = 0.1
collision_distance = 20

# Screen setup
# Sets up window with specified dimensions and title
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')

# Turns off automatic screen updates for smoother rendering
screen.tracer(0)

# Create turtle player
# Initiates the player object, represented by a turtle
player = Player()

# Create cars
# Initiates the car manager object, responsible for generating and managing cars
car_manager = CarManager()

# Create a scoreboard
# Initiates the scoreboard object, responsible for keep track of games statistics
scoreboard = Scoreboard()

# Listen for key events to control player movement
# Registers the 'Up' arrow key press to move the player turtle upward
screen.listen()
screen.onkey(fun=player.go_up, key='Up')

# Game loop control and screen update
# Manages the main game loop, updating the screen and handling game events
game_is_on = True
while game_is_on:
    # Sleeps briefly to control the game's speed
    sleep(seconds)

    # Update the screen to reflect the current game state
    screen.update()

    # Manages the creation and movement of cars on the screen
    # PENDING: Logic to avoid cars overlapping with each other
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collisions with cars
    # Iterates through all cars on the screen and checks if the player turtle is within collision distance
    for car in car_manager.all_cars:
        if car.distance(player) < collision_distance:
            player.collision_detected()
            game_is_on = False

    # Check if player reaches the top edge
    # Verifies if the player turtle has reached the top edge of the screen
    if player.reach_top_edge():
        player.go_to_start_position()
        car_manager.car_move_increment()
        scoreboard.increase_level()

# Exit the game when the screen is clicked
# Allows the user to close the game window by clicking on it
screen.exitonclick()
