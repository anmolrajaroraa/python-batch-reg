Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-2.py ====
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-2.py ====
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-2.py ====
>>> 
==== RESTART: /Users/anmolrajarora/Documents/python-batch-reg/turtle-2.py ====
>>> '''
*
**
***
****
*****
'''
'\n*\n**\n***\n****\n*****\n'
>>> for i in range(10):
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
>>> for i in range(10):
	print('*', end='\n')

	
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
	print('*', end='')

	
**********
>>> for i in range(10):
	for j in range(5):
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
*
*
*
*
*
>>> for i in range(10):
	for j in range(5):
		print('*', end='\n')

		
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
*
*
*
*
*
>>> for i in range(10):
	for j in range(5):
		print('*', end='')

		
**************************************************
>>> for i in range(10):
	for j in range(5):
		print('*', end='')
	print('\n')

	
*****

*****

*****

*****

*****

*****

*****

*****

*****

*****

>>> for i in range(10):
	for j in range(5):
		print('*', end='')
	print()

	
*****
*****
*****
*****
*****
*****
*****
*****
*****
*****
>>> for i in range(10):
	for j in range(i+1):
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
**********
>>> 
>>> for i in range(10):
	for j in range(i+1):
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
**********
>>> '''
    *
   **
  ***
 ****
*****
'''
'\n    *\n   **\n  ***\n ****\n*****\n'
>>> print('hello' ,'world')
hello world
>>> print('hello' ,'world', sep='$$$')
hello$$$world
>>> for i in range(10):
	for k in range(10 - (i+1)):
		print(' ', end='')
	for j in range(i+1):
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
**********
>>> for i in range(10,0,-1):
	for k in range(i-1):
		print(' ', end='')
	for j in range(i+1):
		print('*', end='')
	print()

	
         ***********
        **********
       *********
      ********
     *******
    ******
   *****
  ****
 ***
**
>>> for i in range(10,0,-1):
	for k in range(i-1):
		print(' ', end='')
	for j in range(10 - (i-1)):
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
**********
>>> for i in range(10,0,-1):
	counter = i
	for j in range(counter):
		print(' ', end='')
	for k in range(10 - counter):
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
>>> for i in range(10,0,-1):
	counter = i
	for j in range(counter):
		print('$', end='')
	for k in range(10 - counter):
		print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$**
$$$$$$$***
$$$$$$****
$$$$$*****
$$$$******
$$$*******
$$********
$*********
>>> '''
    *
   ***
  *****
 *******
*********
'''
'\n    *\n   ***\n  *****\n *******\n*********\n'
>>> for i in range(10,0,-1):
	counter = i
	for j in range(counter):
		print('$', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$
>>> for i in range(10,0,-1):
	counter = i
	for j in range(counter):
		print('$', end='')
	for k in range((10 - counter) * 2):
		print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$**
$$$$$$$$****
$$$$$$$******
$$$$$$********
$$$$$**********
$$$$************
$$$**************
$$****************
$******************
>>> for i in range(10,0,-1):
	counter = i
	for j in range(counter):
		print('$', end='')
	for k in range(((10 - counter) * 2) -1):
		print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$***
$$$$$$$*****
$$$$$$*******
$$$$$*********
$$$$***********
$$$*************
$$***************
$*****************
>>> list(range(-1))
[]
>>> list(range(0,-10,-1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> for i in range(20):
	counter = i
	for j in range(10 - counter):
		print('$', end='')

		
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
>>> for i in range(20):
	counter = i
	for j in range(10 - counter):
		print('$', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$










>>> for i in range(20):
	counter = i
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(counter):
			print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$**
$$$$$$$***
$$$$$$****
$$$$$*****
$$$$******
$$$*******
$$********
$*********










>>> for i in range(20):
	counter = i
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(counter):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('$', end='')
		for k in range(9 - counter):
			print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$**
$$$$$$$***
$$$$$$****
$$$$$*****
$$$$******
$$$*******
$$********
$*********
$
$$
$$$
$$$$
$$$$$
$$$$$$
$$$$$$$
$$$$$$$$
$$$$$$$$$
$$$$$$$$$$
>>> for i in range(20):
	counter = i
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(counter):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('$', end='')
		for k in range(19 - counter):
			print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$**
$$$$$$$***
$$$$$$****
$$$$$*****
$$$$******
$$$*******
$$********
$*********
$*********
$$********
$$$*******
$$$$******
$$$$$*****
$$$$$$****
$$$$$$$***
$$$$$$$$**
$$$$$$$$$*
$$$$$$$$$$
>>> for i in range(20):
	counter = i
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('$', end='')
		for k in range(19 - counter):
			print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$***
$$$$$$$*****
$$$$$$*******
$$$$$*********
$$$$***********
$$$*************
$$***************
$*****************
$*********
$$********
$$$*******
$$$$******
$$$$$*****
$$$$$$****
$$$$$$$***
$$$$$$$$**
$$$$$$$$$*
$$$$$$$$$$
>>> for i in range(20):
	counter = i
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('$', end='')
		for k in range(((19 - counter) * 2) - 1):
			print('*', end='')
	print()

	
$$$
$$$$$$$
$$$$$$$$$*
$$$$$$$$***
$$$$$$$*****
$$$$$$*******
$$$$$*********
$$$$***********
$$$*************
$$***************
$*****************
$*****************
$$***************
$$$*************
$$$$***********
$$$$$*********
$$$$$$*******
$$$$$$$*****
$$$$$$$$***
$$$$$$$$$*
$$$$$$$$$$
>>> for i in range(20):
	counter = i
	if i==10:
		continue
	if i<10:
		for j in range(10 - counter):
			print('$', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('$', end='')
		for k in range(((19 - counter) * 2) - 1):
			print('*', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$*
$$$$$$$$***
$$$$$$$*****
$$$$$$*******
$$$$$*********
$$$$***********
$$$*************
$$***************
$*****************
$$***************
$$$*************
$$$$***********
$$$$$*********
$$$$$$*******
$$$$$$$*****
$$$$$$$$***
$$$$$$$$$*
$$$$$$$$$$
>>> for i in range(20):
	counter = i
	if i==10:
		continue
	if i<10:
		for j in range(10 - counter):
			print('', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print('', end='')
		for k in range(((19 - counter) * 2) - 1):
			print('*', end='')
	print()

	

*
***
*****
*******
*********
***********
*************
***************
*****************
***************
*************
***********
*********
*******
*****
***
*

>>> for i in range(20):
	counter = i
	if i==10:
		continue
	if i<10:
		for j in range(10 - counter):
			print(' ', end='')
		for k in range(2 * counter - 1):
			print('*', end='')
	else:
		for j in range(counter - 9):
			print(' ', end='')
		for k in range(((19 - counter) * 2) - 1):
			print('*', end='')
	print()

	
          
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
          
>>> 
