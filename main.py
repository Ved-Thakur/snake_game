import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Ved's Snake game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

resume = True


def resume_game():
    global resume
    resume = True
    scoreboard.reset()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(resume_game, "r")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if resume:
        snake.move()
    collision_with_wall = snake.turtles[0].xcor() > 299 or snake.turtles[0].xcor() < -299 or snake.turtles[
        0].ycor() > 299 or snake.turtles[
                              0].ycor() < -299

    if food.distance(snake.turtles[0]) <= 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if collision_with_wall:
        scoreboard.game_over()
        snake.reset()
        resume = False

    for segment in snake.turtles[1:]:
        if segment.distance(snake.turtles[0]) < 10:
            scoreboard.game_over()
            snake.reset()
            resume = False

screen.exitonclick()
