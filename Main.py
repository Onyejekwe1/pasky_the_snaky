from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pasky The Snaky")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_ongoing = True
while game_ongoing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check if pasky has eaten a turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        scoreboard.game_over()

    for body in snake.bodies[1:]:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 10:
            scoreboard.reset()
screen.exitonclick()
