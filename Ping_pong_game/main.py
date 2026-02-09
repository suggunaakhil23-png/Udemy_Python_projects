from turtle import Turtle, Screen
from create import Create
from center_line import CenterLine
from ball import Ball
import time
from scoreboard import score
from scoreboard1 import score1

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

create = Create()
line = CenterLine()
ball = Ball()
scorea = score()
scoreb = score1()

screen.listen()
screen.onkey(create.up, "w")
screen.onkey(create.down, "s")
screen.onkey(create.up1, "Up")
screen.onkey(create.down1, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.mov()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(create.head1) < 50:
        ball.bounce_x()

    if ball.distance(create.head) < 50:
        ball.bounce_x()
    
    if ball.xcor() > 390 :
        game_is_on = False
    
    if ball.xcor() < -390:
        game_is_on = False

screen.exitonclick()
