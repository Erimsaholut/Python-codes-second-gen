from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()

        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = randint(-14, 14)
        y_cor = randint(-14, 14)
        self.goto(x_cor * 20, y_cor * 20)


