from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=4, outline=None)
paddle.setheading(90)
paddle.penup()
paddle.color("white")
paddle.goto(350, 0)
screen.exitonclick()
