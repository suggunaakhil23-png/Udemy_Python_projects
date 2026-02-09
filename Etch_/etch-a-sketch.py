import turtle as t

turtle = t.Turtle()

def move_forward():
    turtle.forward(100)
def mov_backward():
    turtle.backward(100)
def mov_left():
    turnhead = turtle.heading() + 10.0
    turtle.setheading(turnhead)
def mov_right():
    turnhead = turtle.heading() - 10.0
    turtle.setheading(turnhead)



screen = t.Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=mov_left)
screen.onkey(key="s",fun=mov_backward)
screen.onkey(key="d",fun=mov_right)
screen.exitonclick()