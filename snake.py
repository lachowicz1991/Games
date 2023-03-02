import turtle
from turtle import Screen, Turtle
from time import sleep

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tempo = 1
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        t = Turtle(shape='square')
        t.penup()
        t.color('white')
        t.goto(position)
        t.penup()
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def increase_speed(self):
        self.tempo += 1
        self.speed(self.tempo)

    def reset(self):
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]








