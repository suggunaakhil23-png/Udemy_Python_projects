from turtle import Turtle

class CenterLine:
    def __init__(self):
        self.line = Turtle()
        self.line.hideturtle()
        self.line.color("white")
        self.line.penup()
        self.line.goto(0, -300)
        self.line.setheading(90)
        self.draw()

    def draw(self):
        for _ in range(30):
            self.line.pendown()
            self.line.forward(20)
            self.line.penup()
            self.line.forward(20)
