from turtle import Screen, Turtle, tracer
import time
import random

class Ball(Turtle):


    def __init__(self, go):
        super().__init__()
        self.ball_state = []
        self.go = go
        self.make_a_ball(go)
        self.ballstate = self.ball_state[0]     
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def make_a_ball(self, go):  
        self.penup()
        self.goto(go)
        self.shape("circle")
        self.setheading(90)
        self.color("white")
        self.shapesize(1, 1)
        self.ball_state.append(self)
    
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def clear_ball(self):
        self.ht()

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.5
        print(self.move_speed)

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
