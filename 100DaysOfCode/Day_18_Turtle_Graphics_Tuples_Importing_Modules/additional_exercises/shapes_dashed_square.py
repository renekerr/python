from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

t.color('black')
t.shape('circle')
t.shapesize(0.2)

# Dashed square
for _ in range(4):
    for _ in range(10):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
    t.right(90)


scr.exitonclick()
