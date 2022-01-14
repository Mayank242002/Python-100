from turtle import Turtle

class Ball:

    def __init__(self):
        self.ball=Turtle("circle")
        self.ball.color("white")
        self.ball.shapesize(2,2)
        self.ball.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
        
    def move(self):
        new_x=self.ball.xcor()+self.x_move
        new_y=self.ball.ycor()+self.y_move
        self.ball.goto(new_x,new_y)

    def bounce(self):
        self.y_move*=-1
        

    def bounce2(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def update(self):
        self.ball.goto(0,0)
        self.move_speed=0.1
        self.bounce2()