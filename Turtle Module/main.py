from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("blue2")

for _ in range(15):
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()

screen.exitonclick()
