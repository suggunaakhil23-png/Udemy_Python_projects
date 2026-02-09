from turtle import Turtle,Screen

my_timmy_turtle = Turtle()
my_timmy_turtle.shape("turtle")
my_timmy_turtle.color("red")

def draw_square(value):
    my_timmy_turtle.forward(value)
    my_timmy_turtle.left(90)
    my_timmy_turtle.forward(value)
    my_timmy_turtle.left(90)
    my_timmy_turtle.forward(value)
    my_timmy_turtle.left(90)
    my_timmy_turtle.forward(value)
    my_timmy_turtle.left(90)

draw_square(100)

screen = Screen()
screen.exitonclick()