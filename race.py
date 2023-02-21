import random
import turtle
from turtle import Turtle, Screen
from tkinter import *
from tkinter import messagebox

root = Tk()

  # The alert.

#

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
user_bet = screen.textinput(title='Make your bets!', prompt='Which turtle will win the race? Enter a color')
colors = ['red', 'orange', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
turtle_gang = []
for turtle_index in range(0, 5):
    t = Turtle(shape='turtle')
    t.penup()
    t.goto(x=-230, y=y_position[turtle_index])
    t.color(colors[turtle_index])
    turtle_gang.append(t)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for t in turtle_gang:
        if t.xcor() > 230:
            is_race_on = Falseis_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f'{winner} won the race. Well done for picking a winer!')
                messagebox.showinfo("showinfo", f"'{winner} won the race. Well done for picking a winer!'")
                
            else:
                print(f'Too bad {winner} won the race.')
                messagebox.showinfo("showinfo", f'Too bad {winner} won the race.')
        turtle_distance = random.randint(0, 10)
        t.forward(turtle_distance)
root.mainloop()

screen.exitonclick()

#
# t = Turtle()
# w = Turtle()
# w.color('red')
# s = Screen()
#
# s.listen()
#
# def move_forwards():
#     t.forward(10)
#
# def move_backwards():
#     t.backward(10)
#
#
# def r_left():
#     t.left(10)
#
#
# def r_right():
#     t.right(10)
#
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
#
#
# s.listen()
# s.onkey(key='w', fun=move_forwards)
# s.onkey(key='s', fun=move_backwards)
# s.onkey(key='a', fun=r_left)
# s.onkey(key='d', fun=r_right)
# s.onkey(key='space', fun=clear)
#
#
# s.exitonclick()