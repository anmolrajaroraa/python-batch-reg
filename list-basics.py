Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
*
**
***
****
*****
'''
'\n*\n**\n***\n****\n*****\n'
>>> for i in range(10):
	for i range(i):
		
SyntaxError: invalid syntax
>>> for i in range(10):
	for j in range(i):
		print('*')

		
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>>> for i in range(10):
	for j in range(i):
		print('*', end='')
	print()

	

*
**
***
****
*****
******
*******
********
*********
>>> for i in range(10):
	print('*' * i, end='')
	print()

	

*
**
***
****
*****
******
*******
********
*********
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> length = input("How many elements you want to enter: ")
How many elements you want to enter: 10
>>> list1 = []
>>> for i in range(10):
	element = input(f"Enter element for {i} position: ")
	list1.append(element)

	
Enter element for 0 position: 1
Enter element for 1 position: 2
Enter element for 2 position: 3
Enter element for 3 position: 4
Enter element for 4 position: 5
Enter element for 5 position: 43
Enter element for 6 position: 3
Enter element for 7 position: 45
Enter element for 8 position: 5
Enter element for 9 position: 4
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4']
>>> list1.append(12,23)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list1.append(12,23)
TypeError: append() takes exactly one argument (2 given)
>>> list1.extend(12,23)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list1.extend(12,23)
TypeError: extend() takes exactly one argument (2 given)
>>> list1.extend([12,23])
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23]
>>> list1.append([12,23])
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23]]
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23]]
>>> list2 = list1
>>> list2
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23]]
>>> type(list1)
<class 'list'>
>>> print(['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12,23]])
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23]]
>>> id(list1)
4340806024
>>> hex(id(list1))
'0x102bb7188'
>>> hex(id(list2))
'0x102bb7188'
>>> list1.append('hello')
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello']
>>> list2
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello']
>>> newList = list1.copy()
>>> hex(id(list1))
'0x102bb7188'
>>> hex(id(newList))
'0x1054db508'
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello']
>>> newList
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello']
>>> newList.append('bye')
>>> newList
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello', 'bye']
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23], 'hello']
>>> #copy() creates a shallow copy
>>> 
>>> newList[-3]
[12, 23]
>>> newList[-3].append('new')
>>> newList
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new'], 'hello', 'bye']
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new'], 'hello']
>>> 
>>> 
>>> newList[-3]
[12, 23, 'new']
>>> list1[-2]
[12, 23, 'new']
>>> id(newList[-3]) == id(list1[-2])
True
>>> 
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new'], 'hello']
>>> list4
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new'], 'hello']
>>> list4[-2].append('old')
>>> list4
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new', 'old'], 'hello']
>>> list1
['1', '2', '3', '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new'], 'hello']
>>> id(list1[-2]) == id(list4[-2])
False

>>> list4[2] = 0
>>> list4
['1', '2', 0, '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new', 'old'], 'hello']
>>> list4.insert(2, 0)
>>> list4
['1', '2', 0, 0, '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new', 'old'], 'hello']
>>> #list4[2] = 0     will remove the previous value
>>> #insert() will push the values ahead but not delete them
>>> 
>>> list4
['1', '2', 0, 0, '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new', 'old'], 'hello']
>>> list4.index('4')
4
>>> list4.count('4')
2
>>> list4.index('4', 5)
10
>>> list4.index('4', 11)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    list4.index('4', 11)
ValueError: '4' is not in list
>>> list5 = []
>>> list5[0] = 'hello'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    list5[0] = 'hello'
IndexError: list assignment index out of range
>>> list5 = ['anmol']
>>> list5[0] = 'hello'
>>> list5
['hello']
>>> list4.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    list4.sort(reverse=True)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> list6 = [4343,232,234,5,6,7,8]
>>> list6.sort()
>>> list6
[5, 6, 7, 8, 232, 234, 4343]
>>> list6 = [4343,232,234,5,6,7,8]
>>> list6.sort(reverse=True)
>>> list6
[4343, 234, 232, 8, 7, 6, 5]
>>> list4.sort()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    list4.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> list4
['1', '2', 0, 0, '4', '5', '43', '3', '45', '5', '4', 12, 23, [12, 23, 'new', 'old'], 'hello']
>>> list6 = ['ahcjc','23243', '$', '~', ' ']
>>> list6.sort()
>>> list6
[' ', '$', '23243', 'ahcjc', '~']
>>> list6 = ['ahcjc','23243', '$', '~', ' ', 'anmol']
>>> list6.sort()
>>> list6
[' ', '$', '23243', 'ahcjc', 'anmol', '~']
>>> list7 = [['anmol', 'ram', 'shyam'], ['1234', '1234'], ['#@$', '%$^']]
>>> list7.sort()
>>> list7
[['#@$', '%$^'], ['1234', '1234'], ['anmol', 'ram', 'shyam']]
>>> list7 = [['anmol', 'ram', 'shyam'], ['1234', '1234'], ['#@$', '%$^', '~']]
>>> list7.sort()
>>> list7
[['#@$', '%$^', '~'], ['1234', '1234'], ['anmol', 'ram', 'shyam']]
>>> list7 = [['anmol', 'ram', 'shyam'], ['1234', '1234'], ['#@$', '%$^', '~'], ['#@$', '%$^', ' ']]
>>> 
>>> list7.sort()
>>> list7
[['#@$', '%$^', ' '], ['#@$', '%$^', '~'], ['1234', '1234'], ['anmol', 'ram', 'shyam']]
>>> list8 = [[101, 'Anmol'], [102, 'Ram'], [103, 'Shyam']]
>>> list8.sort()
>>> list8
[[101, 'Anmol'], [102, 'Ram'], [103, 'Shyam']]
>>> list8 = [[101, 'Anmol'], [104, 'Ram'], [103, 'Shyam']]
>>> list8.sort()
>>> list8
[[101, 'Anmol'], [103, 'Shyam'], [104, 'Ram']]
>>> list8 = [[101, 'Anmol'], [104, 'Ram'], [104, 'Shyam']]
>>> list8.sort()
>>> list8
[[101, 'Anmol'], [104, 'Ram'], [104, 'Shyam']]
>>> list8 = [[101, 'Anmol'], [104, 'Ram'], [104, 'Mohan']]
>>> list8.sort()
>>> list8
[[101, 'Anmol'], [104, 'Mohan'], [104, 'Ram']]
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py ====
166 -51
-255 -323
201 -235
-208 192
-143 107
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py", line 31, in <module>
    t.circle(50)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1991, in circle
    self._go(l)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 2469, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py ====
-210 -85
-347 93
305 247
255 -340
323 61
-155 -102
-264 200
51 -132
-205 -276
-283 194
-12 140
-235 -205
31 75
113 172
61 -270
-335 89
-123 -173
102 318
34 6
-160 -334
270 -219
223 -4
-37 -230
-111 -23
-144 -136
23 240
264 264
86 -347
200 174
-206 127
-165 -116
-31 294
-149 -59
3 -43
342 187
53 266
-100 -216
303 -152
-322 -74
-24 79
3 -115
333 -124
238 -153
83 -191
134 -186
-196 -63
33 236
-14 -60
-258 216
-102 99
105 6
-16 -322
293 -278
-155 -257
299 -315
-240 -12
-101 -21
-55 193
-183 33
-292 212
-330 -139
-276 306
-101 -40
52 264
-112 -213
93 -38
-193 -63
-322 237
323 -63
-89 -209
82 -323
220 -309
93 32
13 321
318 118
129 -283
318 45
347 -75
97 305
70 150
19 254
157 68
184 21
-39 107
60 -304
107 -99
-120 -28
246 -48
58 -149
-194 -348
161 205
155 -271
239 -218
-127 -235
172 -103
150 177
-159 -79
180 192
230 -4
104 -233
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py ====
Shape not found
-299 131
-187 316
Shape not found
-80 152
Shape not found
-78 175
252 45
Shape not found
-96 255
Shape not found
85 -163
Shape not found
-29 78
Shape not found
17 -114
Shape not found
-198 -208
173 -147
-261 -147
Shape not found
-65 -259
161 141
139 79
Shape not found
33 161
Shape not found
63 326
Shape not found
-298 -283
Shape not found
2 252
Shape not found
42 -34
Shape not found
-283 -41
Shape not found
-303 278
Shape not found
-130 219
Shape not found
-37 170
115 -172
Shape not found
-184 259
-345 -339
Shape not found
-182 123
Shape not found
329 118
Shape not found
219 -25
43 114
228 -88
Shape not found
-259 117
Shape not found
-247 -63
Shape not found
270 -235
Shape not found
-96 37
Shape not found
251 87
Shape not found
199 -144
Shape not found
-136 -245
Shape not found
-304 -305
Shape not found
-250 212
Shape not found
-98 -85
Shape not found
-41 -224
Shape not found
83 -350
Shape not found
237 -45
Shape not found
-98 251
Shape not found
272 -307
Shape not found
83 255
235 29
Shape not found
142 -78
Shape not found
99 -35
Shape not found
-279 231
Shape not found
342 -180
Shape not found
-110 -127
325 -238
Shape not found
123 127
Shape not found
-128 -91
Shape not found
143 -274
Shape not found
-19 -106
Shape not found
184 5
Shape not found
-210 57
Shape not found
72 91
Shape not found
-347 -266
Shape not found
133 233
-19 -85
Shape not found
27 -228
Shape not found
-124 47
Shape not found
-282 -166
Shape not found
-331 -175
Shape not found
274 102
Shape not found
-15 -347
-284 213
Shape not found
-84 -94
-17 -203
-23 234
-255 252
Shape not found
92 -199
Shape not found
-92 -125
Shape not found
101 160
334 -155
Shape not found
146 40
-219 -44
-243 -92
Shape not found
-165 59
Shape not found
80 -288
Shape not found
-325 -8
Shape not found
338 84
Shape not found
15 -273
Shape not found
-341 167
Shape not found
193 310
Shape not found
-136 -349
Shape not found
-328 44
Shape not found
9 203
Shape not found
172 -162
Shape not found
-346 -72
Shape not found
14 275
-223 -261
83 -9
Shape not found
163 278
Shape not found
24 104
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py ====
Cannot draw triangle
Cannot draw circle
Cannot draw dot
Cannot draw hexagon
-122 343
Cannot draw triangle
Cannot draw circle
Cannot draw dot
Cannot draw hexagon
-63 331
Cannot draw square
Cannot draw triangle
Cannot draw dot
Cannot draw hexagon
258 145
Cannot draw square
Cannot draw triangle
Cannot draw dot
Cannot draw hexagon
-15 197
Cannot draw square
Cannot draw triangle
Cannot draw dot
Cannot draw hexagon
190 6
Cannot draw square
Cannot draw circle
Cannot draw dot
Cannot draw hexagon
274 -245
Cannot draw square
Cannot draw circle
Cannot draw dot
Cannot draw hexagon
53 -195
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py", line 20, in <module>
    t.color(random.choice(colors))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2216, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: gold
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-4.py ====
14 3
241 -347
-72 -170
26 128
-243 -300
-214 -321
31 -239
-206 -345
-27 54
5 258
-332 -13
-302 248
161 -294
262 -151
47 242
146 213
-59 -300
62 69
68 -71
224 266
-336 280
269 -141
189 241
123 258
149 151
-331 -179
102 309
-39 288
-56 -272
329 115
-295 -32
209 -29
-109 52
255 -87
-47 -6
-249 -197
-243 6
-53 -161
97 -121
176 29
-271 261
-181 -95
-347 115
-59 250
143 166
-194 -343
79 -194
-222 329
-247 -292
253 55
-265 -110
326 123
-318 63
-289 81
181 -179
-238 -269
-260 -215
172 18
297 -304
126 -96
138 -97
-202 242
104 55
-220 -163
-193 107
212 342
-22 42
76 -95
55 -225
110 -201
152 -199
-256 101
241 -333
133 -137
309 266
23 252
242 9
-19 170
-35 -311
91 -233
78 166
-296 1
-140 96
69 -47
153 -80
346 35
156 209
-43 -106
248 36
-200 -15
-174 222
179 -345
-254 -270
-263 -120
228 -338
-335 119
-24 -342
104 -139
-43 97
-298 -192
>>> 
