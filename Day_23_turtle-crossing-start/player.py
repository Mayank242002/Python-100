from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle=Turtle("turtle")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)
        

    def player_movement(self):
        self.turtle.forward(MOVE_DISTANCE)

    def start_again(self):
        self.turtle.goto(STARTING_POSITION)
