from turtle import *
from time import sleep
from random import randint



class object(Turtle):
    def __init__(self, x, y, shape='circle', color='red', step=10):

        super().__init__()
        
        
        self.penup()
        self.color(color)
        self.shape(shape)
        self.goto(x, y)
        
        
    
        
        
        #sleep(1)

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        return dist < 25
    
    def obj_set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_start, self.y_start, self.x_end, self.y_end)



    

        
    

    
        

    
    
player = object(0, 0, color='green')
scr = player.getscreen()
#scr.setup(500, 500)
finish = object(0, 400, shape='triangle', color='yellow')
object1 = object(200, 100, color='red', shape='square')
object2 = object(-200, 300, color='red', shape='square')

def down():
    player.goto(player.xcor(), player.ycor() - 5)

def up():
    player.goto(player.xcor(), player.ycor() + 5)

def right():
    player.goto(player.xcor() + 5, player.ycor())

def left():
    player.goto(player.xcor() - 5, player.ycor())



scr.listen()
scr.onkey(right, 'd')
scr.onkey(down, 's')
scr.onkey(up, 'w')
scr.onkey(left, 'a')
object1.obj_set_move(object1.xcor(), object1.ycor(), 400, object1.ycor())

object2.obj_set_move(object1.xcor(), object1.ycor(), 400, object1.ycor())

#sleep(5)
while True:
    object1.set_move()
    object2.set_move()
    
    if player.is_collide(finish):
        player.write("ПОБЕДА")
        break
    if player.is_collide(object1):
        player.write('ПОРАЖЕНИЕ')
        break
    if player.is_collide(object2):
        player.write('ПОРАЖЕНИЕ')
        break
    
    






