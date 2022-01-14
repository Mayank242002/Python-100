from turtle import Turtle

class scoreboard():

    def __init__(self):

        self.score_turtle=Turtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()
        
    def update_score(self):
        self.score_turtle.goto(-100,200)
        self.score_turtle.clear()
        self.score_turtle.write(self.l_score,False,"center",font=("Courier", 70,"normal"))
        self.score_turtle.goto(100,200)
        self.score_turtle.write(self.r_score,False,"center",font=("Courier", 70,"normal"))

    
        