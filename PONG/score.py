from turtle import Screen, Turtle, tracer
import time

class Score(Turtle):
    GAMEOVERTEXT = "GAME OVER!"
    SCOREFONT = ("Courier", 75, "normal")
    G_OVERFONT = ("Courier", 45, "normal")
    ALIGNMENT = "center"
    r_xpos = 80
    r_ypos = 200
    l_xpos = -80
    l_ypos = 200

    def __init__(self, scored):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.r_score = 0
        self.l_score = 0



    def draw_score(self):
        self.clear()
        self.goto(self.l_xpos, self.l_ypos)
        self.write(f"{self.l_score}", align=self.ALIGNMENT, font=self.SCOREFONT)
        self.goto(self.r_xpos, self.r_ypos)
        self.write(f"{self.r_score}", align=self.ALIGNMENT, font=self.SCOREFONT)

    def update_score(self, scored):
        if scored == "r":
            self.r_score += 1
            self.draw_score()
        elif scored == "l":
            self.l_score += 1
            self.draw_score()
        else:
            pass
    
    def check_win(self):
        if self.l_score == 3 or self.r_score == 3:
            return True

    def game_over(self):
        self.goto(0,0)
        if self.r_score == 3:
            self.write(f"     GAME OVER\n Right Player Wins!", align=self.ALIGNMENT, font=self.G_OVERFONT)
        elif self.l_score == 3:
            self.write(f"     GAME OVER\n Left Player Wins!", align=self.ALIGNMENT, font=self.G_OVERFONT)