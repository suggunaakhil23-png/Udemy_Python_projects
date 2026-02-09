import random as Random
import turtle as t

screen = t.Screen()
screen.setup(height=900, width=900)

colors = ["red", "blue", "green", "yellow", "purple"]
coordinates = [-80.0, -40.0, 0.0, 40.0, 80.0]

all_turtles = []
for i in range(5):
    t1 = t.Turtle()
    t1.shape("turtle")
    t1.color(colors[i])
    t1.penup()
    t1.setx(-300)
    t1.sety(coordinates[i])
    all_turtles.append(t1)

movement = [10.0, 20.0, 30.0, 40.0]

user_select = screen.textinput("Which turtle do you bet on?", "Choose: red / blue / green / yellow / purple")

race_on = True
while race_on:
    for t1 in all_turtles:
        move = Random.choice(movement)
        t1.forward(move)

        if t1.xcor() >= 300:
            winner = t1.pencolor()
            print(f"The winner is: {winner}")

            if user_select and user_select.lower() == winner:
                print("You won the bet!")
            else:
                print("You lost the bet!")

            race_on = False
            break

screen.exitonclick()
