from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.add_screen_score()

    def add_right(self):
        self.right_score += 1

    def add_left(self):
        self.left_score += 1

    def add_screen_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=('Courier',55,"normal"))
        self.goto(100,200)
        self.write(self.right_score, align="center", font=('Courier',55,"normal"))
