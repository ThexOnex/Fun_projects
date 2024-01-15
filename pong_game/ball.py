from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#000000")
        self.penup()
        self.left_right = 10
        self.up_down = 10
        self.speed_up = 0.1

    def move(self):
        new_x = self.xcor() + self.left_right
        new_y = self.ycor() + self.up_down
        self.goto(new_x, new_y)

    def go_opposite_direction_y(self):
        self.up_down *= -1

    def go_opposite_direction_x(self):
        self.left_right *= -1
        # increase speed
        self.speed_up *= 0.9

    def reset_ball(self):
        self.reset()
        self.__init__()
        self.speed_up = 0.1
