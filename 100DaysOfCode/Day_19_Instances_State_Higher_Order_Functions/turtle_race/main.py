from turtle import Turtle, Screen
from random import randint, shuffle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
shuffle(colors)
turtle_team = []
winners = []

screen = Screen()
screen.setup(width=500, height=400)
print('Welcome to turtle race 🐢!')
screen.title('Welcome to turtle race 🐢🏁!')

bet_ok = False
is_race_on = False
user_bet = ''

# Draw start line
# Turtle heading: E = 0, N = 90, W=180, S = 270
start_line = Turtle()
start_line.hideturtle()
start_line.penup()
start_line.goto(x=-210, y=150)
start_line.left(90)
start_line.pendown()
start_line.color('silver')
start_line.forward(-300)
start_line.speed('fastest')

# Draw finish line
# Turtle heading: E = 0, N = 90, W=180, S = 270
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(x=220, y=-150)
finish_line.left(90)
finish_line.pendown()
finish_line.color('dark gray')
finish_line.forward(300)
finish_line.speed('fastest')

while not bet_ok:
    user_bet = screen.textinput(title='Make your bet', prompt='Which tutle will win the race? Enter a color: ')
    if user_bet in colors:
        bet_ok = True
        screen.title(f'Your bet: {user_bet}')
        print(f'Your bet: {user_bet}')

pos_x = -230
pos_y = -100

for turtle_idx in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=pos_x, y=pos_y)
    new_turtle.color(colors[turtle_idx])
    new_turtle.speed('fastest')
    pos_y += 40
    turtle_team.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_team:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()  # return/set pencolor
            winners.append(turtle.pencolor())
            if len(winners) == 1:
                if winning_turtle == user_bet:
                    print(f'You have won 🎊🎉🎊!. The {winning_turtle} turtle is the winner!')
                else:
                    print(f'You have lost 😞!. The {winning_turtle} turtle is the winner!')
            elif len(winners) > 1:
                if winning_turtle == user_bet:
                    print(f'It is a draw 😞!')
                    print('Winners are: ')
                    for w in winners:
                        print(f'\t -{w}-')
                else:
                    print(f'You have lost 😞!')
                    print('Winners are: ')
                    for w in winners:
                        print(f'\t -{w}-')

        random_distance = randint(1, 10)
        turtle.forward(random_distance)

print('Game over.')
screen.exitonclick()
