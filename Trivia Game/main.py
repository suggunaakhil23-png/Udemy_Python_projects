from tkinter import *
import requests

window = Tk()
window.title("Trivia App")
window.minsize(width=600,height=800)

canvas = Canvas(width=600, height=800, bg="#9bdeac", highlightthickness=0)
title = canvas.create_text(300, 100, text="Welcome To Trivia", fill="white", font=("Roboto", 35, "italic"))
question = canvas.create_text(300, 400, text="", fill="white", font=("Roboto", 35, "bold"))
canvas.pack()
window.mainloop()