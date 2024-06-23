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

data = pandas.read_csv('spain_cities.csv')
all_cities = data.city.to_list()

game_over = False
while not game_over:
    user_value = screen.textinput(f"{score}/{total_cities} Cities of Spain", 'Enter a city:').title()
    print(user_value)
    if user_value in all_cities:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        check_city = data[data.city == user_value]
        x_coordinate = float(check_city.x)
        y_coordinate = float(check_city.y)
        t.goto(x_coordinate, y_coordinate)
        t.write(arg=check_city.city.item(), align='left', font=("Arial", 8, "normal"))
        score += 1

    if score == 52:
        game_over = True

screen.exitonclick()