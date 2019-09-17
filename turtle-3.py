import turtle
import random

s = turtle.Screen()
t = turtle.Pen()
s.bgcolor('black')
t.speed(0)
#t.color('yellow')
t.shape('turtle')
#s.screensize(1400,700)
#t.turtlesize(2,2)
#t.width(3)
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']
x_coor = list(range(-350, 350))
y_coor = list(range(-350, 350))

for i in range(100):
    t.color(random.choice(colors))
    #t.dot(5 * i)
    t.dot(25)
    t.penup()
    x = random.choice(x_coor)
    y = random.choice(y_coor)
    print(x,y)
    t.setposition(x,y)
    t.pendown()
