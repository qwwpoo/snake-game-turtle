from turtle import Screen
from snake import Snake 
from food import Food
from scor import Score
from moor import Extra
from Timer import Timer
import time

game_on = True
window = Screen()
window.setup(1.0,1.0)
window.bgcolor('black')
window.title('welcome in game snake')
window.tracer(0)

snake = Snake()
food = Food()
scor = Score()
extra = Extra()
timer = Timer(extra)

window.listen()
window.onkey(snake.right,'Right')
window.onkey(snake.left,'Left')
window.onkey(snake.down,'Down')
window.onkey(snake.up,'Up')

start = time.time()
while game_on:
 snake.move()
 window.update()
 time.sleep(0.1)

 # ظهور الـ Extra كل 120 ثانية لو مش ظاهر حاليا
 if time.time() - start > 50 and not extra.is_visible:
   extra.appearr()
   start = time.time()

 # جمع الطعام العادي
 if snake.head.distance(food) < 15:
  food.appear()
  snake.extand()
  scor.more() 

 # جمع الـ Extra
 if snake.head.distance(extra) < 15 and extra.is_visible:
  extra.hideturtle()
  extra.is_visible = False
  num_add = snake.exrand_more()
  scor.more_ex(point = num_add)

 # الاصطدام بالحواف
 if (snake.head.xcor() > 650 or snake.head.xcor() < -670 or
     snake.head.ycor() > 360 or snake.head.ycor() < -300):
   game_on = False

 # الاصطدام بجسم الثعبان
 for sagment in snake.turtle[:-1]:	
  if snake.head.distance(sagment) < 10:
   game_on = False

scor.game_over()   
window.exitonclick()
