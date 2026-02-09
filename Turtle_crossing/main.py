from turtle import Turtle,Screen
import time as time
from movement import Movement
from cars import cars

screen = Screen()
screen.tracer(0) 
screen.listen()
screen.setup(width=600, height=600)
ch = Movement()
car = cars()
screen.onkey(ch.move,"w")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.mov_cars()
    for c in car.all_cars:
        if c.distance(ch.turtle) < 20:
            game_is_on = False
screen.exitonclick()