from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.score = 0
        self.penup()
        self.goto(-55, 260)
        self.write(f"Score: {self.score} ", move=False, align='left', font=('Arial', 25, 'normal'))

    def eat_food(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", move=False, align='left', font=('Arial', 25, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(-120, 0)
        self.write("Game over", move=False, align='left', font=('Arial', 50, 'normal'))
        self.goto(-110, -50)
        self.write(f"Your final score is: {self.score} ", move=False, align='left', font=('Arial', 25, 'normal'))


