from constants import *
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameoverbox import custom_messagebox
import time

def lose():
    global game_on
    snake.die(screen)
    game_on=False    
    custom_messagebox(title="Game Over", message=f'You have lost, achieving a \n score of {scoreboard.score}',icon_path=r"C:\Users\Henrique\Documents\python\100days\day_20_21\snakegame\snake.png")
    screen.bye()    
def win():
    global game_on
    snake.celebrate(screen)
    game_on=False
    custom_messagebox(title="You win", message=f'You have won, achieving the maximum score of {scoreboard.score}! Incredible!',icon_path="snake.png")
    screen.bye()
screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('SnakeGame+')
screen.tracer(0)
snake=Snake(SNAKE_START_SIZE)
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(lambda:snake.turn_snake('up'),"Up")
screen.onkey(lambda:snake.turn_snake('down'),"Down")
screen.onkey(lambda:snake.turn_snake('left'),"Left")
screen.onkey(lambda:snake.turn_snake('right'),"Right")
screen.onkey(lambda:snake.turn_snake('up'),"Up")
game_on=True
while game_on:
    screen.update() 
    snake.move_snake()        
    if snake.hit_tail() or snake.hit_wall():
        lose()
    if snake.head.distance(food.xcor(),food.ycor())<=5:
        snake.grow()
        food.refresh(snake)
        scoreboard.add_score()
    if scoreboard.score>=MAX_SCORE:
        win()
    time.sleep(0.1)
exit()
    
     
    

    