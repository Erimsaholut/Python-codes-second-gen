from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.turtles_first_x_axis = 0
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.goto(self.turtles_first_x_axis, 0)
            snake.color("White")
            snake.penup()
            self.snakes.append(snake)
            self.turtles_first_x_axis -= 20

    def extend_snake(self):
        snake = Turtle(shape="square")
        snake.goto(500, 0)
        snake.color("White")
        snake.penup()
        self.snakes.append(snake)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
