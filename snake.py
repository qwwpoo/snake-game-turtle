from turtle import Turtle
import random
class Snake():
 def __init__(self):
  self.turtle = []
  self.colors = ['aqua','blue','brown','gray','lime','magenta','navy'
  ,'orange','pink','purple',
  'silver','teal','white','yellow','green']

  self.loc = [[-80,0], [-60,0], [-40,0], [-20,0], [0,0]]
  self.pudy()
  self.head = self.turtle[-1]
  self.head.color(random.choice(self.colors))
 def pudy(self):
  for i in range(len(self.loc)): 
   new_snake = Turtle('square')
   new_snake.speed('fast')
   new_snake.penup()
   new_snake.goto(self.loc[i])
   new_snake.color('white')
   self.turtle.append(new_snake)
   
 def move(self):
  for i in range(len(self.turtle)-1):
   self.turtle[i].goto(self.turtle[i+1].pos()) 
  self.head.forward(20)	 
 def extand(self):
  new_food = Turtle('square')
  new_food.color('white')  
  new_food.penup()
  self.turtle.insert(0,new_food)
  
 def right(self):
   self.head.setheading(0)
 def left(self):
   self.head.setheading(180)
 def up(self):
  self.head.setheading(90)
 def down(self):
  self.head.setheading(270)