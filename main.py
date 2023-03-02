from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

food = Food()
scoreboard = Scoreboard()
snake = Snake()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()


    #Collision with food
    if snake.head.distance(food) < 15:
        print("Ulumulu")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    for segnent in snake.segments[1:]:
        # if segnent == snake.head:
        #     continue
        if snake.head.distance(segnent) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()