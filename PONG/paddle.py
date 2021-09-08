from turtle import Screen, Turtle, tracer
import time

class Paddle(Turtle):

    def __init__(self, go):
        super().__init__()
        self.paddle_state = []
        self.go = go
        print("Makin da paddl's!")
        self.create_paddle(go)
        self.pad = self.paddle_state[0]


    def create_paddle(self, go):
        # paddle = Turtle()
        self.penup()
        self.goto(go)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.paddle_state.append(self)
        print(self.paddle_state)


    def move_paddle_up(self):
        if self.pad.ycor() == 250:
            pass
        else:
            y_cord = self.pad.ycor() + 50
            self.pad.goto(self.pad.xcor(), y_cord)
            print("moving up")

    def move_paddle_down(self):
        if self.pad.ycor() == -250:
            pass
        else:
            y_cord = self.pad.ycor() - 50
            self.pad.goto(self.pad.xcor(), y_cord)
            print("moving down")

    



