# TODO Convert the guess to Title case
# TODO Check if the guess is among the 50 states
# TODO Write correct guesses onto the map
# TODO Use a loop to allow the user to keep guessing
# TODO Record the correct guesses in a list
# TODO Keep track of the score
import csv
import turtle

screen = turtle.Screen()
screen.title('Spain Cities Game')
image = 'spain.gif'
screen.addshape(image)
turtle.shape(image)

user_value = screen.textinput('Cities of Spain', 'Enter a city:').title()

with open('spain_cities.csv') as data_file:
    cities_of_spain = csv.reader(data_file)

"""
# Function to get coordinates
def get_mouse_click_coordinates(x, y):
    print(f",{x},{y}")

turtle.onscreenclick(get_mouse_click_coordinates)
turtle.mainloop()
"""
