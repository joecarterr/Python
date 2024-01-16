from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.goto(coordinate)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.update_text()
    
    def update_text(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.update_text()
