from turtle import Turtle


class Scoreboard:

     def __init__(self):
        global file
        self.score_turtle=Turtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.goto(0,270)
        self.score_turtle.hideturtle()
        file=open("Day_20_Snake_Game/data.txt","r")
        self.score_value=0
        self.high_score=file.read()
        self.final_score="Score:"+str(self.score_value)+" | High Score:"+self.high_score
        self.score_turtle.write(self.final_score,False,"center",font=('Arial', 20, 'normal'))
        
    
     def increase(self):
        file=open("Day_20_Snake_Game/data.txt","w")
        self.score_value+=1
        if (self.score_value>int(self.high_score)):
            self.high_score=self.score_value
            file.write(str(self.high_score))
        self.final_score="Score:"+str(self.score_value)+" | High Score:"+str(self.high_score)
        self.score_turtle.clear()
        self.score_turtle.write(self.final_score,False,"center",font=('Arial', 20, 'normal'))

     def Game_over(self):
        self.score_turtle.goto(0,0)
        self.score_turtle.write("GAME OVER",False,"center",font=('Arial', 20, 'normal'))
        file.close()
       
        
    
    