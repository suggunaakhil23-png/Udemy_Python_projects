from turtle import Turtle
import random as random
colors = ["red","green","orange","purple","blue","yellow","brown"]
start_move_distance = 5
move_distance = 10

class cars:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_number = random.randint(1,6)
        if(random_number == 1):
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1,stretch_len=2)
                new_car.penup()
                new_car.color(random.choice(colors))
                random_y = random.randint(-200,250)
                new_car.goto(300,random_y)
                self.all_cars.append(new_car)
    
    def mov_cars(self):
        for car in self.all_cars:
            car.backward(start_move_distance)

