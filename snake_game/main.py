from snake import Snake
import time
from turtle import Screen
from food import Food
from score import Scoreboard


def you_lost_mssg():
    my_score.clear()
    my_score.game_over()
    # time.sleep(0.5)
    # my_score.clear()
    my_snake.reseted()
    my_food.reappear()
    Scoreboard.scores_variable = 0
    


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game :)")
screen.tracer(0)
# turn off animation

my_snake = Snake()
my_food = Food()

my_score = Scoreboard()


screen.listen()


screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.down, "Down")


still_playing = True
while still_playing:
    # show results
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # the snake ate the food

    if my_snake.head.distance(my_food) < 18:
        my_food.reappear()
        my_score.clear()
        # snakes grows more
        my_snake.grow()
        # delete the previous command
        my_score = Scoreboard()

    # the snake hit the wall

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        you_lost_mssg()
        # break

    # snake bit itself

    for body_part in my_snake.full_body[1:]:
        if my_snake.head.distance(body_part) < 10:
            you_lost_mssg()
            # still_playing = False




screen.exitonclick()
