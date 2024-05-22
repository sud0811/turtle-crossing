from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(x=-220, y= 260)
        self.write ( arg=f"LEVEL: {self.score}", align="center", font=('Courier', 24, 'normal'))
        self.hideturtle()

    def game_over(self):
         self.goto(0,0)
         self.write ( arg='Game over.', align="center", font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write ( arg=f"LEVEL: {self.score}", align="center", font=('Courier', 24, 'normal'))
