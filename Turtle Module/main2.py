from turtle import Turtle, Screen
import random

timmy = Turtle() 
timmy.hideturtle()
colors = ["red", "green", "blue", "purple", "pink", "black", "orange"]
timmy.width(4)

num_of_sides = 2

while num_of_sides <= 10:
    random_color = random.choice(colors)
    timmy.color(random_color)
    num_of_sides += 1
    for _ in range(num_of_sides):
        timmy.fd(100)
        angle = 360 / num_of_sides
        timmy.right(angle)
