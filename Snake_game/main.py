from scoreboard import Scoreboard
from Screen import Ekran
from snake import Snake
from time import sleep
from food import Food

ekran = Ekran()
snaker = Snake()
food = Food()

scoreboard = Scoreboard()


ekran.listen()
ekran.onkey(snaker.up, "Up")
ekran.onkey(snaker.down, "Down")
ekran.onkey(snaker.left, "Left")
ekran.onkey(snaker.right, "Right")


game_is_on = True


while game_is_on:
    ekran.screen_update()
    sleep(0.1)
    snaker.move()

    if snaker.head.xcor() >= 300 or snaker.head.xcor() <= -310:
        scoreboard.game_over()
        game_is_on = False

    if snaker.head.ycor() >= 310 or snaker.head.ycor() <= -310:
        scoreboard.game_over()
        game_is_on = False

    if snaker.head.distance(food) < 19:
        food.refresh()
        scoreboard.eat_food()
        snaker.extend_snake()

    for snakes in snaker.snakes[1:]:
        if snaker.head.distance(snakes) < 10:
            scoreboard.game_over()
            game_is_on = False


ekran.exit()
