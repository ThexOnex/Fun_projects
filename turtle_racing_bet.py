import random
from turtle import Turtle, Screen

still_racing = False

screen = Screen()


# set the pop up size
screen.setup(500, 400)
UserBet = screen.textinput(
    title="Your bet", prompt="(red, purple, blue, black, yellow, green) Enter a turtle color: ")

turtle_colors = ["red", "purple", "blue", "black", "yellow", "green"]
my_turtles = []


for y, c in zip(range(0, 150, 25), range(len(turtle_colors))):
    player = Turtle(shape="turtle")
    player.up()
    player.color(turtle_colors[c])
    player.goto(x=-230, y=-72+y)
    my_turtles.append(player)

if UserBet:
    still_racing = True

while still_racing:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            still_racing = False
            winner = turtle.pencolor()
            if winner == UserBet:
                print(f"YOU HAVE WON!!!"
                      f"{winner} turtle have won the race !!!")
            else:
                print(f"You lost! {winner} turtle is the winner")
        random_distant = random.randint(0, 10)
        turtle.forward(random_distant)
        # color() method returns a tuple of color values, and the [0] index is used to access the primary color
        # if u want to make a certain color to win
        # if turtle.color()[0] == "color":
        #     turtle.forward(10)

screen.exitonclick()
 