from turtle import Turtle
from snake import Snake
import random
from constants import *
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("pink")
        random_x=random.randrange(-limitx,limitx+20,20)
        random_y=random.randrange(-limity,limity+20,20)
        self.goto(random_x,random_y)
    def refresh(self,snake:Snake):
        pos_set={(x,y) for x in range(-limitx,limitx+20,20) for y in range(-limity,limity+20,20)}
        snakecurr=snake.head
        while snakecurr:
            pos_set.discard((snakecurr.xcor(),snakecurr.ycor())) 
            snakecurr=snakecurr.next
        rand_pos=random.choice(list(pos_set))
        self.goto(rand_pos[0],rand_pos[1])
        
    
        
