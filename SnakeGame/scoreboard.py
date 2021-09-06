from turtle import Turtle


class Score(Turtle):
    TEXT = "Score: "
    GAMEOVERTEXT = "GAME OVER!"
    FONT = ("Arial", 18, "normal")
    ALIGNMENT = "center"
    score = 0
    xpos = 0
    ypos = 250

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.goto(self.xpos, self.ypos)
        self.write(f"{self.TEXT} {self.score}", align=self.ALIGNMENT, font=self.FONT)
        # self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"{self.TEXT} {self.score}", align=self.ALIGNMENT, font=self.FONT)
        # self.refresh()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"{self.GAMEOVERTEXT}", align=self.ALIGNMENT, font=self.FONT)
        
        