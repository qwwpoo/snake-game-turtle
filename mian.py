from turtle import Screen
from snake import Snake 
from food import Food
from scor import Score
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


window.listen()
window.onkey(snake.right,'Right')
window.onkey(snake.left,'Left')
window.onkey(snake.down,'Down')
window.onkey(snake.up,'Up')
while game_on:
 snake.move()
 window.update()
 time.sleep(0.1)
 if snake.head.distance(food) < 15:
  food.appear()
  snake.extand()
  scor.more()
 if (snake.head.xcor() > 640 or snake.head.xcor() < -670 or
    snake.head.ycor() > 360 or snake.head.ycor() < -300):
    game_on = False 
 for sagment in snake.turtle[:-1]:	
  if snake.head.distance(sagment) < 10	:
   game_on = False
scor.game_over()   

  
window.exitonclick()