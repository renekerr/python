from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Manages the creation and movement of cars on the screen."""

    def __init__(self):
        self.all_cars = []
        self.car_positions = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.total_cars = 0

    def create_car(self):
        """Creates a new car at a random y-position and adds it to the list."""
        random_y = randint(-240, 250)
        if randint(1, 10) == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.setheading(180)
            color = choice(COLORS)
            new_car.color(color)
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=3)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars forward by the current car_speed."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_move_increment(self):
        """Increases the car_speed by MOVE_INCREMENT."""
        self.car_speed += MOVE_INCREMENT
