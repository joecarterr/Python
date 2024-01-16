# IMPORTS:
from turtle import Turtle, Screen
import random

# SETTING-UP:
dot = Turtle()
screen = Screen()
screen.setup(width=800, height=800)

# CREATING A TUPLE OF ALL THE DOT COLOURS:
screen.colormode(255)
colour_list = [(215, 166, 17), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42)]

# CONSTANTS:
STARTING_POSITION_X = -365
STARTING_POSITION_Y = -355
WALL_X_COR = 355
DOT_SIZE = 30
DOT_MOVEMENT_SIZE = 80  # (50px total gap because 80px - 30px (dot size))
NUMBER_OF_DOTS = 100

# DOT STARTING VALUES:
dot.penup()
dot.hideturtle()
dot.goto(STARTING_POSITION_X, STARTING_POSITION_Y)
dot.speed("fastest")
        

# CHANGING THE HEIGHT OF THE DOT WHEN IT HAS MADE 10 DOTS:
def change_y_cor(x_cor, y_cor):
    dot.penup()
    # **if the dots x coordinate is greater than the width of the screen then move the dot upwards and start on a new line**
    if int(x_cor) >= WALL_X_COR:
        y_cor += DOT_MOVEMENT_SIZE  # ensuring an equal amount of space either side of the circle (50px)
        dot.sety(y_cor)
        dot.setx(STARTING_POSITION_X)


# MAKING 100 DOTS: (10x10 grid style)
for _ in range(NUMBER_OF_DOTS):
    y = dot.ycor()
    x = dot.xcor()
    # changing dots colour:
    random_colour_tuple = random.choice(colour_list)
    dot.pencolor(random_colour_tuple)
    dot.dot(DOT_SIZE)
    dot.penup()
    dot.fd(DOT_MOVEMENT_SIZE)
    dot.pendown()
    # calling the y-coordiante function:
    change_y_cor(x_cor=x, y_cor=y)

screen.exitonclick()
