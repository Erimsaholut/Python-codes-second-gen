from turtle import Turtle, Screen, colormode

tospa = Turtle()
ekran = Screen()
ekran.colormode(255)


def move_fd():
    tospa.fd(30)


def move_bd():
    tospa.fd(-30)


def move_clk():
    new_angle = tospa.heading() + 10
    tospa.setheading(new_angle)


def move_cclk():
    new_angle = tospa.heading() - 10
    tospa.setheading(new_angle)


def clear():
    tospa.home()
    tospa.clear()




ekran.listen()
ekran.onkey(key="w", fun=move_fd)
ekran.onkey(key="s", fun=move_bd)
ekran.onkey(key="a", fun=move_cclk)
ekran.onkey(key="d", fun=move_clk)
ekran.onkey(key="c", fun=clear)


ekran.exitonclick()
