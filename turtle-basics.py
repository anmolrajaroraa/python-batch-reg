Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.turtlesize(2,2,2)
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> t.width(5)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.color('yellow')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> t.color('green')
>>> for i in [0,1,2,3]{
	
SyntaxError: invalid syntax
>>> for i in [0,1,2,3]:
	t.forward(100)
	t.left(90)

	
>>> for i in range(4):
	t.forward(100)
	t.left(90)

	
>>> c = input("How many times you want turtle to run? ")
How many times you want turtle to run? 10
>>> for i in range(c):
	t.forward(100)
	t.left(90)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i in range(c):
TypeError: 'str' object cannot be interpreted as an integer
>>> c = int(c)
>>> for i in range(c):
	t.forward(100)
	t.left(90)

	
>>> t.circle(100)
>>> t.dot(50)
>>> t.reset()
>>> t.color('pink')
>>> t.color('red')
>>> for i in range(3):
	t.forward(100)
	t.left(60)

	
>>> for i in range(8):
	t.forward(100)
	t.left(60)

	
>>> t.color('blue')
>>> for i in range(4):
	t.forward(100)
	t.left(60)

	
>>> for i in range(2):
	t.forward(100)
	t.left(60)

	
>>> t.reset()
>>> for i in range(3):
	t.forward(100)
	t.left(120)

	
>>> size = 100
>>> for i in range(50):
	size = size + 5
	for i in range(3):
		t.forward(size)
		t.left(120)

		
>>> t.speed(0)
>>> t.reset()
>>> for i in range(50):
	size = size + 5
	for i in range(3):
		t.forward(size)
		t.left(120)

		
Traceback (most recent call last):
  File "<pyshell#73>", line 4, in <module>
    t.forward(size)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1637, in forward
    self._go(distance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3179, in _goto
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 562, in _update
    self.cv.update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1177, in update
    self.tk.call('update')
KeyboardInterrupt
>>> t.reset()
>>> t.speed(0)
>>> for i in range(50):
	size = size + 5
	for i in range(3):
		t.forward(size)
		t.left(120)

		
>>> t.reset()
>>> t.speed(0)
>>> t.color('yellow')
>>> for i in range(50):
	for i in range(3):
		t.forward(10*i)
		t.left(120)

		
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)

		

>>> t.reset()
>>> t.speed(0)
>>> t.color('red')
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)

		
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
		t.backward(5)

		
>>> t.reset()
>>> t.speed(0)
>>> t.color('red')
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
		t.backward(5)

		
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
		t.backward(15)

		
>>> t.reset()
>>> t.speed(0)
>>> t.color('red')
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
	t.backward(5)

	
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
t.backward(50)
SyntaxError: invalid syntax
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)
    print('hello')
    
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(50):
	for j in range(3):
		t.forward(10*i)
		t.left(120)

		
>>> 
turtle.Pen()
turtle.bgcolor()
turtle.screensize(1000,500)
