from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_num = 1
        self.goto(-290, 260)
        self.write(f"Level:{self.level_num}", align="left", font=FONT)

    def level_plus(self):
        self.clear()
        self.level_num += 1
        self.write(f"Level:{self.level_num}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.home()
        self.write("GAME OVER", align="left", font=FONT)
