from turtle import Turtle,Screen
import random
class Food():

    def __init__(self):
        self.food=Turtle("circle")
        self.food.color("blue")
        self.food.penup()
        self.food.speed("fastest")
        self.food.shapesize(0.5,0.5)
        self.rand()

        
    def rand(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.food.goto(random_x,random_y)


        



