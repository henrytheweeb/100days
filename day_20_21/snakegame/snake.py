from turtle import Turtle,Screen
import time
from constants import *
class SnakeBlock(Turtle):
    def __init__(self,x,y,next=None,prev=None):
        super().__init__()
        self.shape("square")
        self.pen(fillcolor="white",outline=1)
        self.pu()
        self.goto(x=x,y=y)
        self.next:SnakeBlock=next
        self.prev:SnakeBlock=prev    
class Snake:
    def __init__(self, size):        
        self.head = SnakeBlock(0, 0)  # Head of the snake
        current = self.head
        prev_block = None
        
        # Create the rest of the blocks
        for _ in range(1, size):
            new_block = SnakeBlock(x=current.xcor() - 20, y=0, prev=current)
            current.next = new_block
            prev_block = current  # Update previous block
            current = new_block  # Move to the newly created block
        
        self.tail = current  # Tail of the snake
        #setup old tail location
        self.oldtail=SnakeBlock(0,0)
        self.oldtail.hideturtle()
    def move_snake(self):
        self.oldtail.goto(self.tail.xcor(),self.tail.ycor())        
        snakecurr=self.tail
        while snakecurr.prev:
            snakecurr.goto(snakecurr.prev.xcor(),snakecurr.prev.ycor())
            snakecurr=snakecurr.prev        
        snakecurr.forward(20)
    def die(self,screen):
        snakecurr=self.head
        while snakecurr:
            snakecurr.pen(fillcolor="red",outline=1)
            screen.update()
            time.sleep(0.1)
            snakecurr=snakecurr.next 
    def celebrate(self,screen):
        rainbow=['red','orange','yellow','green','blue','blue4','purple4']
        color_counter=0
        snakecurr=self.head
        while snakecurr:
            snakecurr.pen(fillcolor=rainbow[color_counter%7],outline=1)
            color_counter+=1
            screen.update()
            time.sleep(0.1)
            snakecurr=snakecurr.next
    def hit_wall(self):
        return abs(self.head.xcor())>limitx or abs(self.head.ycor())>limity
    def hit_tail(self):
        snakecurr=self.head.next
        while snakecurr:
            if snakecurr.distance(self.head.xcor(),self.head.ycor())<10:
                return True
            snakecurr=snakecurr.next
        return False
    def grow(self):
        current=self.tail #get current tail
        self.tail=SnakeBlock(self.oldtail.xcor(),self.oldtail.ycor(),prev=current)
        current.next=self.tail
        
        
    def turn_snake(self,dir:str):
        direction_dic={
            'up':90,
            'down':270,
            'right':0,
            'left':180
        }
        if self.head.heading()%180!=direction_dic[dir]%180:
            self.head.setheading(direction_dic[dir])
        

        