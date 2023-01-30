import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

BOUNDRY_UP = 280
RIGHT_AND_LEFT_BOUNDRY = 340
DISTANCE = 50
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
# creating paddle's using paddle class
screen.tracer(0)
paddle_Left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

# key handler
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_Left.up, "w")
screen.onkey(paddle_Left.down, "s")
game_is_on = True
ball = Ball()
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > BOUNDRY_UP or ball.ycor() < -1 * BOUNDRY_UP:
        ball.bounce_y()
    if (ball.xcor() > RIGHT_AND_LEFT_BOUNDRY and paddle_right.distance(ball) <= DISTANCE) or (
            ball.xcor() < -1 * RIGHT_AND_LEFT_BOUNDRY and paddle_Left.distance(ball) <= DISTANCE):
        ball.bounce_x()
        ball.bounce_y()

screen.exitonclick()
