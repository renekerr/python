from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

t.color('black')
t.shape('circle')
t.shapesize(0.2)

# Drawing a square
for _ in range(4):
    t.forward(100)
    t.right(90)


scr.exitonclick()