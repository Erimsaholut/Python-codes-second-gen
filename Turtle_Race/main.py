from turtle import Turtle, Screen
import random

ekran = Screen()
user_bet = ekran.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
is_race_on = False
ekran.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "pink"]
all_racers = []
deg = 150

for i in range(6):
    turta = Turtle("turtle")
    all_racers.append(turta)
    turta.penup()
    turta.color(colors[i])
    turta.goto(x=-230, y=deg)
    deg -= 55

line = Turtle()
line.speed("fastest")
line.hideturtle()
line.penup()
line.goto(230, 200)
line.pendown()
line.goto(230, -200)
line.goto(210, -200)
line.goto(210, 200)
x = 210
y = 200
for i in range(20):
    x += 20
    line.goto(x, y)
    y -= 20
    line.goto(x, y)
    x -= 20
    line.goto(x, y)
if user_bet:
    is_race_on = True
while is_race_on:
    for turta in all_racers:

        if is_race_on:

            if turta.xcor() > 210:
                is_race_on = False
                winner_color = turta.color()
                turta.setheading(180)
                if winner_color[0] == user_bet:
                    print(f"You win !!! Winner is :{winner_color[0]} ,Your choice is :  {user_bet}")
                else:
                    print(f"You lose :( Winner is :{winner_color[0]} ,Your choice is :  {user_bet}")

        rand_distance = random.randint(0, 10)
        turta.forward(rand_distance)
ekran.exitonclick()
