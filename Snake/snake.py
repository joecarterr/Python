from turtle import Turtle
SQAURE_POSITIONS = [(0, 0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in SQAURE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake:
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            last_segment = self.segments[segment_number]
            new_x_position = self.segments[segment_number - 1].xcor()
            new_y_position = self.segments[segment_number - 1].ycor()
            last_segment.goto(x=new_x_position, y=new_y_position)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
