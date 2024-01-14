import random
from turtle import Turtle
import turtle

up = 90
down = 270
right = 0
left = 180


class Snake:
    half_circle_square = ((-10, 0), (-10, -10), (10, -10), (10, 0), (5, 10), (-5, 10))
    turtle.register_shape("head", half_circle_square)

    def __init__(self):
        self.full_body = []
        self.body = [(0,0),(-10,0),(-30,0)]
        self.create_the_body()
        self.head = self.full_body[0]

    def create_the_body(self):
        for position in self.body:
            if position == self.body[0]:
                self.add_body_part(position,"head")
            else:
                self.add_body_part(position,"square")

    def add_body_part(self, position,shape):
        body_part = Turtle(shape)
        body_part.penup()
        body_part.color("white")
        body_part.goto(position)
        self.full_body.append(body_part)

    def grow(self):
        # add a new body part in the position of the last body part
        self.add_body_part(self.full_body[-1].position(),"square")

    def move(self):
        for body_number in range(len(self.full_body) - 1, 0, -1):  # 2 1 0
            new_x = self.full_body[body_number - 1].xcor()
            new_y = self.full_body[body_number - 1].ycor()
            self.full_body[body_number].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)