from turtle import Turtle,Screen
import turtle
import random

colors=["blue","green","yellow","orange","red"]

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
turtles=[]
y_value=180
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230,y=y_value)
    y_value-=80
Race=True
while Race:
    for turtle in turtles:
        if turtle.xcor()>230:
            Race=False
            Winning_color=turtle.pencolor()
            if (Winning_color==user_bet):
                print("You have won",Winning_color," is the Winner!")
            else:
                print("You have Lost!",Winning_color," is the Winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance )


screen.exitonclick() 