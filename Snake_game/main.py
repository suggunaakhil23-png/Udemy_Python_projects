from turtle import Turtle, Screen
import time
from snake import Snake
from food import food
from scoreboard import score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = food()
score = score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.mov()
    if snake.head.distance(food) < 15:
        food.random_locations()
        snake.extend()
        score.increase()
    if snake.head.xcor() > 280.0 or snake.head.ycor() > 280.0 or  snake.head.xcor() < -280.0 or snake.head.ycor() < -280.0 :
        score.game_over()
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game.over()
            game_is_on - False
screen.exitonclick()
