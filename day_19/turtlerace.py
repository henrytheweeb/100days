from turtle import Turtle, Screen
import random
import math
from collections import defaultdict
#Implemented an alternative race track, with a circular path that remains fair by modifying the speeds of the turtles in respect to the track length
def setup_race(colors:list[str],shape:str):
    turtlearr:list[Turtle]=[]
    nturtles=len(colors)
    if shape=='line':
        for i in range(len(colors)):
            turtlearr.append(Turtle(shape="turtle"))
            turtlearr[i].color(colors[i])
            turtlearr[i].pd()
            turtlearr[i].goto(x=-230,y=180-(i+1)*360/(nturtles+1))
    elif shape=='circle':
        for i in range(len(colors)):
            turtlearr.append(Turtle(shape="turtle"))
            turtlearr[i].color(colors[i])
            turtlearr[i].pu()
            turtlearr[i].goto(x=-200+(i+1)*150/(nturtles+1),y=0)
            turtlearr[i].setheading(90)
            turtlearr[i].pd()                    
    return turtlearr
is_race_on=False       
screen = Screen()
screen.setup(width=500,height=400)
pick_track=screen.textinput(title="Track selection",prompt='Choose track shape (line/circle)')
user_bet=screen.textinput(title="Make your bet!",prompt='Pick the winning turtle(write the color)')
colors=['red','orange','yellow','green','blue', 'purple']
ncolors=len(colors)
turtles:list[Turtle]=setup_race(colors,pick_track)

if user_bet:
    is_race_on=True
if pick_track=='circle':
    sidelen=[2*abs(-200+(i+1)*150/(ncolors+1))*math.tan(math.pi/90) for i in range(ncolors)]
    steps_counter=defaultdict(int)
while is_race_on:
    if pick_track=='line':
        for turtle in turtles:
            dist=random.random()*10
            turtle.forward(dist)
            if turtle.xcor()>230:
                is_race_on=False
                winner=turtle.pencolor()
                if winner==user_bet:
                    print(f"The {winner} turtle has won and so have you!")
                else:
                    print(f"The {winner} turtle has won, better luck next time!")
    if pick_track=='circle':
        for index,turtle in enumerate(turtles):
            steps=random.randint(0,3)
            steps_counter[index]+=steps
            for _ in range(steps):
                turtle.forward(sidelen[index])
                turtle.right(4)
            if steps_counter[index]>90:
                is_race_on=False
                winner=turtle.pencolor()
                if winner==user_bet:
                    print(f"The {winner} turtle has won and so have you!")
                else:
                    print(f"The {winner} turtle has won, better luck next time!")

                













screen.exitonclick()
