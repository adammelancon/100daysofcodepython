from turtle import Turtle, Screen, bgcolor
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(" - PONG - ")


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball((0.00,0.00))
score = Score("none")

score.draw_score()


screen.listen()
# Move right paddle.
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
# Move left paddle.
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    ball.move_ball()
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with top and bottom walls.
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 320 or ball.distance(l_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_x()

    # Detect if ball goes past paddles.
    # Right side.
    if ball.xcor() >= 390:
        score.update_score("l")
        ball.reset_pos()
    # Left side.
    elif ball.xcor() <= -390:
        score.update_score("r")
        ball.reset_pos()      

    # Check for a winner.
    if score.check_win():
        game_is_on = False
        ball.clear_ball()
        score.game_over()
        print("GAME OVER")






screen.exitonclick()
