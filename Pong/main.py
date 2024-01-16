from turtle import Screen
from dotted_line import DottedLine
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

# SCREEN ATTRIBUTES:
SCREEN_COLOUR = "black"
wn = Screen()
wn.setup(height=600, width=600)
wn.bgcolor(SCREEN_COLOUR)
wn.title("Pong")
wn.tracer(0)

# OBJECTS:
scoreboard_1 = Scoreboard((40, 240))
scoreboard_2 = Scoreboard((-40, 240))
l_paddle = Paddles((-270, 0))
r_paddle = Paddles((270, 0))
dotted_line = DottedLine()
ball = Ball()

# CHECKING FOR KEY PRESSES:
wn.listen()
wn.onkeypress(key="w", fun=l_paddle.move_up)
wn.onkeypress(key="s", fun=l_paddle.move_down)
wn.onkeypress(key="Up", fun=r_paddle.move_up)
wn.onkeypress(key="Down", fun=r_paddle.move_down)

# MAIN GAME RUNNING:
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    wn.update()
    dotted_line.draw_line()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 290:
        scoreboard_1.add_score()
        ball.home()
        ball.bounce_x()
    
    if ball.xcor() < -290:
        scoreboard_2.add_score()
        ball.home()
        ball.bounce_x()

    if ball.distance(l_paddle) < 40 or ball.distance(r_paddle) < 40:
        ball.bounce_x()

wn.exitonclick()
