from turtle import Turtle, Screen
import turtle as t
import random

# 10 ver 10 hor
# 20 === 50 ==== 20


def vertical(times):
    for i in range(times):
        dots.forward(50)
        dots.dot(20, random.choice(colors))


def horizontal(times):
    for i in range(-5, times-5):
        dots.goto(-250, 50*i)
        vertical(times)


colors = [(221, 150, 92), (111, 190, 110), (138, 181, 195), (58, 94, 135), (149, 85, 55), (208, 129, 179), (64, 178, 142),
          (186, 42, 78), (182, 81, 145), (230, 85, 52), (13, 172, 216), (246, 171, 163), (83, 41, 105), (164, 217, 207), (48, 53, 47)]


dots = Turtle()
dots.up()
t.colormode(255)
# dots.setpos(-250,-50)
# t.setworldcoordinates(-1, -1, 20, 20)

dots.goto(-250, -100)

horizontal(10)


screen = Screen()
screen.exitonclick()
