import turtle as t
from turtle import Screen
import random

screen = Screen()
spirograph = t.Turtle()
angle = 0
spirograph.width(5)
spirograph.speed("fastest")
screen.bgcolor("black")
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour_choice = (r, g, b)
    return random_colour_choice


for _ in range(52):
    angle += 7
    spirograph.color(random_colour())
    spirograph.circle(120)
    spirograph.setheading(angle)

screen.exitonclick()
