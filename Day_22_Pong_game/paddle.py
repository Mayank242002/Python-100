from turtle import Turtle, ycor

class Paddle:

    def __init__(self,position):
        self.paddle=Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(5,1)
        self.paddle.penup()
        self.paddle.goto(position)
       
    
    def up(self):
        new_y=self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(),new_y)
    
    def down(self):
        new_y=self.paddle.ycor()-20
        self.paddle.goto(self.paddle.xcor(),new_y)
  