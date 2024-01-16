from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)

screen.exitonclick()