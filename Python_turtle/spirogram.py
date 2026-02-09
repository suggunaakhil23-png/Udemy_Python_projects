import random 
import turtle as t

a = int(input("--"))
turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
def color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for x in range(int(360 / a)) :
   turtle.speed("fastest")
   turtle.color(color())
   turtle.circle(100)
   turtle.setheading(turtle.heading() + 10.0)




screen = t.Screen()
screen.exitonclick()