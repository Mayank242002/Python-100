
from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def anti_clockwise():
    tim.left(20)

def clockwise():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s") 
screen.onkey(anti_clockwise,"a") 
screen.onkey(clockwise,"d") 
screen.onkey(clear,"c")
screen.exitonclick()