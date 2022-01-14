from turtle import Screen

from paddle import Paddle
from Ball import Ball
from scoreboard import scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1=Paddle((-380,0))
paddle2=Paddle((380,0))
Ball=Ball()
scoreboard=scoreboard()

screen.listen()

screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")


Game_is_on=True
while Game_is_on:
    time.sleep(Ball.move_speed)
    screen.update()
    Ball.move() 
    
    #when ball collide with uper and lower wall
    if ((Ball.ball.ycor()>=280) or (Ball.ball.ycor()<=-280)):
        Ball.bounce()
    
    #when ball collide with the paddles
    if ((Ball.ball.distance(paddle2.paddle)<50) and (Ball.ball.xcor()>340) or (Ball.ball.distance(paddle1.paddle)<50) and (Ball.ball.xcor()<-340)):
        Ball.bounce2()
    
    #detect when right paddle misses
    if ((Ball.ball.xcor()>380)):
        scoreboard.l_score+=1
        scoreboard.update_score()
        Ball.update()
      

    #detect when left paddle misses
    if ((Ball.ball.xcor()<-380)):
        scoreboard.r_score+=1
        scoreboard.update_score() 
        Ball.update()
      



screen.exitonclick()