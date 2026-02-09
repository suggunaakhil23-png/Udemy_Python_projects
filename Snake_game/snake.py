from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0] 
        self.tail = self.segments[-1]

    def create(self):
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)        # FIXED
        segment.speed("fastest")
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # FIXED

    def mov(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
