from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

up_limit = 280
down_limit = -280
left_limit = -320
right_limit = 320

screen = Screen()
screen.title("My Pong Game :)")
screen.bgcolor("#EBD9B4")
screen.setup(width=800,height=600)
screen.tracer(0)


right_paddle = Paddle()
left_paddle = Paddle()
ball: Ball = Ball()
scoreboard = Scoreboard()

right_paddle.goto(350, 0)
left_paddle.goto(-350, 0)
screen.update()

screen.listen()


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")



still_playing = True
while still_playing:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move()

    # method 2 (better) ball hit up or down
    if ball.ycor() > up_limit or ball.ycor() < down_limit: # go down
        ball.go_opposite_direction_y()

    # ball hit the paddle
    if (40 > ball.distance(right_paddle) and ball.xcor() > right_limit) or (40 > ball.distance(left_paddle) and ball.xcor() < left_limit):
        ball.go_opposite_direction_x()



    # right lost

    if ball.xcor() > right_limit + 50:
        ball.reset_ball()
        ball.left_right = -10
        scoreboard.add_left()
        scoreboard.add_screen_score()


    # left lost

    if ball.xcor() < left_limit - 50:
        ball.reset_ball()
        ball.left_right = 10
        scoreboard.add_right()
        scoreboard.add_screen_score()




screen.exitonclick()