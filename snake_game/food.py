from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5,0.5)
        self.color("plum")
        self.speed("fastest")
        pos_x = random.randint(-270, 270)
        pos_y = random.randint(-270, 270)
        self.goto(pos_x, pos_y)

    def reappear(self):
        pos_x = random.randint(-270, 270)
        pos_y = random.randint(-270, 270)
        self.goto(pos_x, pos_y)