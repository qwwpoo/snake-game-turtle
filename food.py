from turtle import Turtle
from snake import Snake
import random

class Food(Turtle):
 def __init__(self):  
  super().__init__()
  self.color('red')
  self.shape('circle')
  self.shapesize(0.7,0.7)
  self.penup()
  self.appear()
 def appear(self):
  self.goto(random.randint(-630,630),random.randint(-280,340))