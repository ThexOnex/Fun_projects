from turtle import Turtle
up_limit = 280
down_limit = -280


def create_body():
    pad = Turtle()
    pad.shape("square")
    pad.color("white")
    pad.shapesize(stretch_wid=5, stretch_len=1)
    pad.penup()
    return pad


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#BBAB8C")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        if up_limit > self.ycor():
            new_pos_y = self.ycor() + 20
            self.goto(self.xcor(), new_pos_y)

    def move_down(self):
        if down_limit < self.ycor():
            new_pos = self.ycor() - 20
            self.goto(self.xcor(), new_pos)

