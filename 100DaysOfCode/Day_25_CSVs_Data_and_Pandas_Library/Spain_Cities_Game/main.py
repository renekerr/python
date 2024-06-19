# TODO: Convert the guess to Title case (DONE)
# TODO: Check if the guess is among the 52 cities (DONE)
# TODO: Write correct guesses onto the map
# TODO: Use a loop to allow the user to keep guessing
# TODO: Record the correct guesses in a list
# TODO: Keep track of the score
import turtle
import pandas

screen = turtle.Screen()
screen.title('Spain Cities Game')
image = 'spain.gif'
screen.addshape(image)
turtle.shape(image)

total_cities = 52
score = 0

user_value = screen.textinput(f"{score}/{total_cities} Cities of Spain", 'Enter a city:').title()

# Read data from a CSV file into a DataFrame
data = pandas.read_csv('spain_cities.csv')

check_city = data[data['city'] == user_value]
x_coordinate = float(check_city['x'])
y_coordinate = float(check_city['y'])

