"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import colorgram
import turtle
import random as rd
rgb_colors = []
colors = colorgram.extract(
    'dot.jpg', 100)
t = turtle.Turtle()
f_color = colors[0]
rgb = f_color.rgb



for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

turtle.colormode(255)
t.speed('fastest')
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 101
for x in range(1,  num_of_dots):
    t.dot(20, rd.choice(rgb_colors))
    t.forward(50)
    if x % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

