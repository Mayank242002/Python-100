from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    
    def __init__(self):
        self.cars_collection=[]
        self.new_shift_of_cars()

    def new_shift_of_cars(self):
        self.cars_collection.clear()
        for i in range(4):
            for color in COLORS:
                car=Turtle("square")
                car.shapesize(1,2)
                car.color(color)
                car.penup()
                car.goto(random.randint(-280,280),random.randint(-250,250))
                self.cars_collection.append(car)

            

    def keep_moving(self):
        for i in range(4):
            for car in self.cars_collection:
                car.backward(MOVE_INCREMENT)
                if (car.xcor()<-300):
                    car.goto(random.randint(-280,280),random.randint(-250,250))
        
    def increase_speed(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT+=0.3

            
        
        

