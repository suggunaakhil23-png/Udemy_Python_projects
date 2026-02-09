from turtle import Turtle

positions = [
    (-370, 0), (-370, 20), (-370, -20),
    (370, 0), (370, 20), (370, -20)
]

class Create:
    def __init__(self):
        self.pads = []
        self.create()
        self.head = self.pads[0]
        self.head1 = self.pads[3]

    def create(self):
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        segment.speed("fastest")
        self.pads.append(segment)

    def up(self):
        for seg in self.pads[:3]:
            seg.sety(seg.ycor() + 40)

    def down(self):
        for seg in self.pads[:3]:
            seg.sety(seg.ycor() - 40)

    def up1(self):
        for seg in self.pads[3:]:
            seg.sety(seg.ycor() + 40)

    def down1(self):
        for seg in self.pads[3:]:
            seg.sety(seg.ycor() - 40)
