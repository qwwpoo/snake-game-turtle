from turtle import Turtle

class Timer(Turtle):
 def __init__(self, extra):
  super().__init__()
  self.extra = extra
  self.color('cyan')
  self.penup()
  self.hideturtle()
  self.goto(0,260)
  self.update_display()

 def update_display(self):
  self.clear()
  if self.extra.is_visible:
   self.write('Extra disappears in: {}s'.format(self.extra.time_left), align='center', font=('Arial', 20, 'bold'))
  else:
   self.write('Extra is hidden', align='center', font=('Arial', 20, 'bold'))
  self.getscreen().ontimer(self.update_display, 200)  # تحديث كل 0.2 ثانية
