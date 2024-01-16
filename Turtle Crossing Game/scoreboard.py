from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.level = 0
        self.player_level()
        
    def player_level(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
    
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)
