from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.write(f"Score: {self.score} ", align="ALIGNMENT", font=FONT)

    def update_scoreborard(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.write("Game over", ALIGNMENT, FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreborard()
