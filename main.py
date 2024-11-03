from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun= snake.up)
screen.onkey(key="Down", fun= snake.down)
screen.onkey(key="Left", fun= snake.left)
screen.onkey(key="Right", fun= snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_parts()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()


    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Collision with tail
    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
