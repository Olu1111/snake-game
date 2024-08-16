from turtle import *
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(600, 600)          # set up the screen
screen.bgcolor('black')
screen.tracer(0)                            # turn off tracing for snake animation, used to make body appear combined
screen.title('My snake game')

snake = Snake()
food = Food()
score = Score()

screen.listen()                             # screen will now respond to keystrokes
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')        # don't include () after function name
screen.onkey(snake.right, 'Right')

game = True
while game:
    screen.update()             # paired with the tracer method makes body appear together, screen updates after moving
    time.sleep(0.1)
    snake.move()

    # detect snake collision with food
    if snake.body[0].distance(food) < 15:
        score.update()
        snake.grow()
        food.move()

    if snake.body[0].xcor() > 290 or snake.body[0].xcor() < -290:
        snake.loopx()

    if snake.body[0].ycor() > 290 or snake.body[0].ycor() < -290:
        snake.loopy()

    for part in snake.body[1:len(snake.body) - 1]:
        if snake.body[0].distance(part) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
