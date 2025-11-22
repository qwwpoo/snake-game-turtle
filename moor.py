from turtle import Turtle
import random

class Extra(Turtle):
 def __init__(self):
  super().__init__()
  self.color('orange')
  self.penup()
  self.shape('circle')
  self.shapesize(3,3)
  self.hideturtle()
  self.is_visible = False
  self.time_left = 0  # الوقت المتبقي للظهور

 def appearr(self):
  if not self.is_visible:
   self.goto(random.randint(-630,630),random.randint(-280,340))
   self.showturtle()
   self.is_visible = True
   self.time_left = 6  # مدة الظهور بالثواني
   self.update_timer()

 def update_timer(self):
  if self.time_left > 0:
   self.time_left -= 1
   self.getscreen().ontimer(self.update_timer, 1000)
  else:
   self.hideturtle()
   self.is_visible = False
