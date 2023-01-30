from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        super().shape("square")
        super().shapesize(stretch_wid=1, stretch_len=5)
        super().setheading(90)
        super().penup()
        super().color("white")
        super().goto(position)

    def up(self):
        super().forward(30)

    def down(self):
        super().backward(30)
