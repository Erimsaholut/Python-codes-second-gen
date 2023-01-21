from turtle import Screen



class Ekran:
    def __init__(self):
        self.screen = Screen()
        self.create_screen()

    def create_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game ")
        self.screen.tracer(0)

    def screen_update(self):
        self.screen.update()

    def exit(self):
        self.screen.exitonclick()

    def listen(self):
        self.screen.listen()

    def onkey(self, func, key):
        self.screen.onkey(func, key)

