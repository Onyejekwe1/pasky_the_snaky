from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[0]

    def create_snake(self):
        for starting_point in STARTING_POSITIONS:
            self.add_segment(starting_point)

    def add_segment(self, position):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.bodies.append(new_body)

    def extend(self):
        self.add_segment(self.bodies[-1].position())

    def move(self):
        for body in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[body - 1].xcor()
            new_y = self.bodies[body - 1].ycor()
            self.bodies[body].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
