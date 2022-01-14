from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard:
    
    def __init__(self):
        self.score=Turtle()
        self.score.penup()
        self.score.goto(-230,250)
        self.score.hideturtle()
        self.level=0
        self.level_str="Level:"+str(self.level)
        self.score.write(self.level_str,False,"center",FONT)

    def update_score(self):
        self.score.clear()
        self.level+=1
        self.level_str="Level:"+str(self.level)
        self.score.write(self.level_str,False,"center",FONT)

    def GAME_OVER(self):
        self.score.clear()
        self.score.goto(0,0)
        self.score.write("GAME OVER",False,"center",FONT)

