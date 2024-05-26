from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

t.color('black')
t.shape('circle')
t.shapesize(0.2)

# Dashed lines
for _ in range(20):
    t.forward(5)
    t.penup()
    t.forward(5)
    t.pendown()


scr.exitonclick()


"""
# Dashed lines changing color
# for _ in range(10):
#     tommy.forward(15)
#     tommy.color('white')
#     tommy.forward(15)
#     tommy.color('black')
"""