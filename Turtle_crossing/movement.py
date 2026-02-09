from turtle import Turtle

class Movement:
    def __init__(self):
        self.create()
    def create(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.goto(0, -280)
    
    def move(self):
        new_y = self.turtle.ycor() + 10
        self.turtle.sety(new_y)
