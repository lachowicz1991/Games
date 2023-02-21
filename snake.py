from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')


turtle_gang = []
y_position = 0
for turtle_index in range(0, 3):
    t = Turtle(shape='square')
    t.penup()
    t.goto(x=y_position, y=0)
    t.color('white')
    turtle_gang.append(t)
    y_position += 20

screen.exitonclick()