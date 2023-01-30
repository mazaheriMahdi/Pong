from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("square")
        super().shapesize(stretch_wid=1, stretch_len=5)
        super().setheading(90)
        super().penup()
        super().color("white")

    def up(self):
        super().forward(10)

    def down(self):
        super().backward(10)
