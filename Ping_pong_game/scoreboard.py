from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0   
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 370)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score_value}", align="center", font=("Arial", 14, "normal"))

    def increase(self):     
        self.score_value += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 14, "normal"))
