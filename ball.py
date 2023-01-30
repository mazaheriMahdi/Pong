from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().color("white")
        super().penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = super().xcor() + self.x_move
        new_y = super().ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
