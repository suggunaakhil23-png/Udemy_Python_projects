import pandas as pd
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic(r"E:\Udemy Full course\US_States_game\blank_states_img.gif")

data = pd.read_csv(r"E:\Udemy Full course\US_States_game\50_states.csv")
all_states = data.state.to_list()

timer = Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 210)

writer = Turtle()
writer.hideturtle()
writer.penup()

screen.tracer(0)

time_left = 720
guessed = []


def update_timer():
    global time_left
    timer.clear()
    timer.write(f"Time Remaining: {time_left}", align="center", font=("Arial", 18, "normal"))
    screen.update()
    time_left -= 1
    if time_left >= 0:
        screen.ontimer(update_timer, 1000)


update_timer()


while time_left >= 0:
    answer = screen.textinput("Guess the State", "Enter a state name:")
    if answer is None:
        break

    answer = answer.title()

    if answer in all_states and answer not in guessed:
        guessed.append(answer)
        row = data[data.state == answer]
        x = int(row.x.iloc[0])
        y = int(row.y.iloc[0])
        writer.goto(x, y)
        writer.write(answer)

screen.exitonclick()
