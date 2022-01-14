import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car=CarManager()
player=Player()
Score=Scoreboard()

screen.listen()
screen.onkey(player.player_movement,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.keep_moving()

    for i in range(4):
            for i in car.cars_collection:
                if (player.turtle.distance(i)<15):
                    game_is_on=False
                    Score.GAME_OVER()

    if (player.turtle.ycor()>280):
        Score.update_score()
        car.increase_speed()
        player.start_again()


screen.exitonclick()
                
    


    


