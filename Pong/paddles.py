from turtle import Turtle

class Paddles(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.goto(coordinate)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4)

    def move_up(self):
        self.setheading(90)
        self.fd(20)
    
    def move_down(self):
        self.setheading(270)
        self.fd(20)
