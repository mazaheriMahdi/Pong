from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
# creating paddle's using paddle class
paddle_Left = Paddle()
paddle_Left.goto(-350 , 0)
paddle_right = Paddle()
paddle_right.goto(350 , 0)


screen.exitonclick()
