from turtle import Turtle

class Snake:
    def __init__(self):
        starting_positions=[(0,0),(-20,0),(-40,0)]
        self.snake_segements=[]
        for i in starting_positions:
            turtle=Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(i)
            self.snake_segements.append(turtle)

        self.head=self.snake_segements[0]

    def move(self):
        
        for seg_num in range(len(self.snake_segements)-1,0,-1):
            new_x=self.snake_segements[seg_num-1].xcor()
            new_y=self.snake_segements[seg_num-1].ycor()
            self.snake_segements[seg_num].goto(new_x,new_y)
            
        self.snake_segements[0].forward(20)

    def update_snake(self):
        turtle2=Turtle("square")
        turtle2.color("white")
        turtle2.penup()
        turtle2.goto(self.snake_segements[-1].position())
        self.snake_segements.append(turtle2)



    def up(self):
        if (self.snake_segements[0].heading()!=270):
            self.snake_segements[0].setheading(90)

    def down(self):
        if (self.snake_segements[0].heading()!=90):
            self.snake_segements[0].setheading(270)

    def left(self):
        if (self.snake_segements[0].heading()!=0):
            self.snake_segements[0].setheading(180)

    def right(self):
        if (self.snake_segements[0].heading()!=180):
            self.snake_segements[0].setheading(0)


