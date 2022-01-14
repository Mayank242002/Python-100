from turtle import Turtle

class Scoreboard:

     def __init__(self):
        self.score_turtle=Turtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.goto(0,270)
        self.score_turtle.hideturtle()
        self.score_value=0
        self.final_score="Score:"+str(self.score_value)
        self.score_turtle.write(self.final_score,False,"center",font=('Arial', 20, 'normal'))
        
    
     def increase(self):
        self.score_value+=1
        self.final_score="Score:"+str(self.score_value)
        self.score_turtle.clear()
        self.score_turtle.write(self.final_score,False,"center",font=('Arial', 20, 'normal'))

     def Game_over(self):
        self.score_turtle.goto(0,0)
        self.score_turtle.write("GAME OVER",False,"center",font=('Arial', 20, 'normal'))
       
        
    
    