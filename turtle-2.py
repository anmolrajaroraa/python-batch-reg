#print(list(range(4)))

import turtle
import random

s = turtle.Screen()
t = turtle.Pen()
s.bgcolor('black')
t.speed(0)
#t.color('yellow')
t.shape('turtle')
s.screensize(1400,700)
#t.turtlesize(2,2)
#t.width(3)
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']

for i in range(50):
    for j in range(3):
        t.forward(10 * i)
        t.left(120)
    t.penup()
    #color = random.choice(colors)
    t.color(random.choice(colors))
    t.backward(5)
    #t.right(90)
    #t.forward(2.5)
    #t.left(90)
    t.pendown()
