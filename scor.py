from turtle import Turtle

class Score(Turtle):
 def __init__(self):
  super().__init__()
  self.score = 0
  self.color('white')
  self.penup()
  self.goto(0,300)
  self.hideturtle()
  self.update()
  
 def update(self): 
  self.clear()
  self.write('score:{}'.format(self.score),align = "center" , font = ('Arial',24,'normal'))
  
 def more(self,):
  self.score += 1
  self.update()
  
 def more_ex(self,point):
  self.score += point
  self.update()
    
 def game_over(self):
  self.getscreen().bgcolor('darkred')
  self.goto(0,0)
  self.write('game over \n لقد خسرت\n high score:2600\nfinal Score: {}'.format(self.score),align = 'center',font = ('Arial',24,'normal'))
