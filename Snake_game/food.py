from turtle import Turtle
import random as Random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        randomx = Random.randint(-280,300)
        randomy = Random.randint(-280,300)
        self.goto(randomx,randomy)
    def random_locations(self):
        randomx = Random.randint(-280,300)
        randomy = Random.randint(-280,300)
        self.goto(randomx,randomy)