from turtle import Turtle
import time


class Scoreboard(Turtle):
    scores_variable = 0

    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {Scoreboard.scores_variable}", align="center", font=('Courier', 15, 'italic'))
        Scoreboard.scores_variable += 1

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER !!!", align="center", font=('Ariel', 35, 'bold'))
        self.goto(0,-50)
        self.write(f"your highest score: {self.scores_variable-1}", align="center", font=('Ariel', 20, 'italic'))





