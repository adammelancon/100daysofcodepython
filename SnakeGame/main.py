from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:    
    
    time.sleep(.1)
    snake.move()
    if snake.wall_check():
        score.game_over()
        game_on = False
    screen.update()
    # Detect collision with food.
    if snake.head.distance(food) <= 15:
        food.refresh()
        score.refresh()
        snake.grow_snake()

    # Detect collision with snake body.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()