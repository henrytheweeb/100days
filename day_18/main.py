from turtle import Turtle,Screen
import random as rd

tim=Turtle()
tim.shape('turtle')
tim.color("DarkViolet")
screen=Screen()
screen.setup (width=3000, height=3000, startx=0, starty=0)
tim.speed("fastest")

# Draw A Square

#for i in range(4):
#    tim.forward(50)
#    tim.left(90)

#polygons

#for i in range(3,11):
#    tim.pencolor(rd.random()*screen.colormode(),rd.random()*screen.colormode(),rd.random()*screen.colormode())
#    angle=360.0/i
#    for j in range(i):
#        tim.forward(100)
#        tim.right(angle)
    
#random walk

def randomWalk(n_steps):
    tim.width(15) 
    for i in range(n_steps):
        tim.pencolor(rd.random()*screen.colormode(),rd.random()*screen.colormode(),rd.random()*screen.colormode())
        angle=rd.choice([90*i for i in range(4)])
        tim.left(angle)
        tim.forward(30)
       
#Spyrograph
def spyrograph(step,forw=0):
    angle=360./step
    for _ in range(step):
        tim.pencolor(rd.random()*screen.colormode(),rd.random()*screen.colormode(),rd.random()*screen.colormode())
        tim.circle(100)
        tim.left(angle)
        tim.forward(forw)

spyrograph(200,1)




screen=Screen()
screen.exitonclick()
