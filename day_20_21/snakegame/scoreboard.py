from turtle import Turtle
from constants import *
ALIGNMENT="center"
FONT=('Arial',24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.pu()        
        self.goto(x=0,y=limitx-FONT[1])
        self.write(arg=f"Score:{self.score}",align=ALIGNMENT,font=FONT)
    def add_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score:{self.score}",align=ALIGNMENT,font=FONT)
        
        
        
    