from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pasky The Snaky")
screen.tracer(0)

starting_points = [(0, 0), (-20, 0), (-40, 0)]
bodies = []

for starting_point in starting_points:
    new_body = Turtle("square")
    new_body.color("white")
    new_body.penup()
    new_body.goto(starting_point)
    bodies.append(new_body)


game_ongoing = True
while game_ongoing:
    screen.update()
    time.sleep(1)



screen.exitonclick()
