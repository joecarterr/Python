from turtle import Turtle
height_of_screen = 300
NUMBER_OF_DOTTED_LINES = int(height_of_screen / 20)

class DottedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.setheading(270)
        self.width(5)
        self.color("white")
        self.penup()
        self.goto(x=0, y=300)

    def draw_line(self):
        for _ in range(NUMBER_OF_DOTTED_LINES):
            self.down()
            self.fd(20)
            self.up()
            self.fd(20)