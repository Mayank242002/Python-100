
from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food() 
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with the food
    if (snake.head.distance(food.food)<15):
        snake.update_snake()
        food.rand()
        scoreboard.increase()

    #detect collision with the wall
    if ((snake.head.xcor()>290) | (snake.head.xcor()<-290) | (snake.head.ycor()>280) | (snake.head.ycor()<-280)):
        game_is_on=False
        scoreboard.Game_over()

    #detect collision with the tail
    for i in range(1,len(snake.snake_segements)):

        if (snake.head.distance(snake.snake_segements[i])<10):
            print("laddai")
            scoreboard.Game_over()
            game_is_on=False



screen.exitonclick()