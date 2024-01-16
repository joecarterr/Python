from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()
etch.width(4)
etch.speed("fastest")


def left():
    new_heading = etch.heading() + 10
    etch.setheading(new_heading)
    etch.fd(50)


def right():
    new_heading = etch.heading() - 10
    etch.setheading(new_heading)
    etch.fd(50)


def forwards():
    etch.fd(50)


def backwards():
    etch.bk(50)


def clear_screen():
    etch.home()
    etch.clear()  # screen.clear() removes everything so when resetting the screen use turtle.clear() instead. (you can still use the turtle object after the clear.)

screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="space", fun=clear_screen)

screen.mainloop()