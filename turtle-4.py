import turtle
import random

s = turtle.Screen()
t = turtle.Pen()
s.bgcolor('black')
t.speed(0)
t.color('yellow')
t.shape('turtle')
#s.screensize(1400,700)
#t.turtlesize(2,2)
#t.width(3)
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']
x_coor = list(range(-350, 350))
y_coor = list(range(-350, 350))
shapes = list(range(5))
#square, triangle, circle, dot, hexagon

for i in range(100):
    t.color(random.choice(colors))
    shape = random.choice(shapes)
    if shape == 0:
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif shape == 1:
        for i in range(3):
            t.forward(100)
            t.left(120)
    elif shape == 2:
        t.circle(50)
    elif shape == 3:
        t.dot(50)
    else:
        for i in range(6):
            t.forward(100)
            t.left(60)
    '''if shape == 0:
        for i in range(4):
            t.forward(100)
            t.left(90)
    else:
        print('Cannot draw square')



    if shape == 1:
        for i in range(3):
            t.forward(100)
            t.left(120)
    else:
        print('Cannot draw triangle')


            
    if shape == 2:
        t.circle(50)
    else:
        print('Cannot draw circle')


        
    if shape == 3:
        t.dot(50)
    else:
        print('Cannot draw dot')




        
    if shape == 4:
        for i in range(6):
            t.forward(100)
            t.left(60)
    else:
        print('Cannot draw hexagon')'''
    t.penup()
    x = random.choice(x_coor)
    y = random.choice(y_coor)
    print(x,y)
    t.setposition(x,y)
    t.pendown()
