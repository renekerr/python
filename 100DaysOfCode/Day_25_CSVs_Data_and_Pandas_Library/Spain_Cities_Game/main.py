# TODO: Convert the guess to Title case (DONE)
# TODO: Check if the guess is among the 52 cities (DONE)
# TODO: Write correct guesses onto the map (DONE)
# TODO: Use a loop to allow the user to keep guessing (DONE)
# TODO: Record the correct guesses in a list (DONE)
# TODO: Keep track of the score (DONE)
# TODO: Avoid user guess same city (DONE)
# TODO: Hint of how to quit game (DONE)
# TODO: Show score on screen
# TODO: Modularize the code
# TODO: Add some comments

import turtle
import pandas as pd

TEXT_ALIGNMENT = 'center'
TEXT_FONT = ("Arial", 8, "normal")

# Set up the screen
screen = turtle.Screen()
screen.title('Spain Cities Game')
spain_map_image = 'spain.gif'
screen.addshape(spain_map_image)
turtle.shape(spain_map_image)

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.goto(0, -380)
turtle_writer.write(arg="Type 'exit' to quit the game.", align='center', font=("Courier", 15, "normal"))

TOTAL_CITIES = 52
current_score = 0

# Read city data from CSV
city_data = pd.read_csv('spain_cities.csv')
city_list = city_data.city.to_list()
guessed_city_list = []

# Start the game loop
is_game_over = False
while not is_game_over:
    user_guess = screen.textinput(f"{current_score}/{TOTAL_CITIES} Cities of Spain", 'Enter a city:').title()

    if user_guess == 'Exit':
        print('You have successfully exited the game.')
        print(f'Guessed cities = {len(guessed_city_list)}')
        is_game_over = True

    if (user_guess in city_list) and (user_guess not in guessed_city_list):
        city_info = city_data[city_data.city == user_guess]
        turtle_writer.goto(int(city_info.x.iloc[0]), int(city_info.y.iloc[0]))
        city_name = city_info.city.item()
        turtle_writer.write(arg=city_name, align=TEXT_ALIGNMENT, font=TEXT_FONT)
        guessed_city_list.append(city_name)
        current_score += 1

    if len(guessed_city_list) == TOTAL_CITIES:
        is_game_over = True
        turtle_writer.goto(0, 370)
        turtle_writer.write(arg="Congratulations! You've guessed all cities of Spain!", align='center',
                            font=("Courier", 15, "normal"))
        screen.exitonclick()
