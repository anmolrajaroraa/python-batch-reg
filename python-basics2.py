Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = 'python is very easy to learn'
>>> str1.split()
['python', 'is', 'very', 'easy', 'to', 'learn']
>>> #tokenizationx
>>> #my name is anmol
>>> 
SyntaxError: invalid syntax
>>> str1 = 'python is very easy to learn, "python" has easy syntax, and works on indentation only'
>>> str1.split()
['python', 'is', 'very', 'easy', 'to', 'learn,', '"python"', 'has', 'easy', 'syntax,', 'and', 'works', 'on', 'indentation', 'only']
>>> str1.split(',')
['python is very easy to learn', ' "python" has easy syntax', ' and works on indentation only']
>>> str1 = 'python is very easy to learn\n "python" has easy syntax\n and works on indentation only'
>>> str1.splitlines()
['python is very easy to learn', ' "python" has easy syntax', ' and works on indentation only']
>>> str1 = 'python is very easy to learn\n "python" has easy syntax\t and works on indentation only'
>>> print(str1)
python is very easy to learn
 "python" has easy syntax	 and works on indentation only
>>> str1.splitlines()
['python is very easy to learn', ' "python" has easy syntax\t and works on indentation only']
>>> str1 = 'python is very easy to learn\t "python" has easy syntax\t and works on indentation only'
>>> str1.splitlines()
['python is very easy to learn\t "python" has easy syntax\t and works on indentation only']
>>> str1 = 'python is very easy to learn\t "python" has easy syntax\r and works on indentation only'
>>> str1.splitlines()
['python is very easy to learn\t "python" has easy syntax', ' and works on indentation only']
>>> str1 = 'python is very easy to learn\n "python" has easy syntax\t and works on indentation only'
>>> str1.split('\n')
['python is very easy to learn', ' "python" has easy syntax\t and works on indentation only']
>>> str1.split('a')
['python is very e', 'sy to le', 'rn\n "python" h', 's e', 'sy synt', 'x\t ', 'nd works on indent', 'tion only']
>>> str1.partition('a')
('python is very e', 'a', 'sy to learn\n "python" has easy syntax\t and works on indentation only')
>>> str1.find('a')
16
>>> str1.rfind('a')
75
>>> str1.partition('a')
('python is very e', 'a', 'sy to learn\n "python" has easy syntax\t and works on indentation only')
>>> str1.rpartition('a')
('python is very easy to learn\n "python" has easy syntax\t and works on indent', 'a', 'tion only')
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1.sizeof
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    str1.sizeof
AttributeError: 'str' object has no attribute 'sizeof'
>>> str1.sizeof()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    str1.sizeof()
AttributeError: 'str' object has no attribute 'sizeof'
>>> str1.__sizeof__
<built-in method __sizeof__ of str object at 0x103d0c608>
>>> str1.__sizeof__)
SyntaxError: invalid syntax
>>> str1.__sizeof__()
134
>>> import sys
>>> sys.getsizeof(str1)
134
>>> str1.__class__
<class 'str'>
>>> 'python'.__le__('java')
False
>>> 'python'.__ge__('java')
True
>>> 'python' > 'java'
True
>>> #isdecimal() works for all the digits from 0 to 9
>>> #isdigit() works for all the digits as well as superscript and subscript
>>> #isnumeric() works for fractions as well
>>> input('What''s your name')
Whats your name
''
>>> input('What\'s your name')
What's your nameAnmol
'Anmol'
>>> str1 = 'abc\def'
>>> str1
'abc\\def'
>>> str1 = 'abc\\def'
>>> str1
'abc\\def'
>>> str1 = 'abc\ndef'
>>> print(str)
<class 'str'>
>>> print(str1)
abc
def
>>> str1
'abc\ndef'
>>> str1 = "let's learn \"python\""
>>> str1
'let\'s learn "python"'
>>> print(str1)
let's learn "python"
>>> str1 = 'abc\ndefn'
>>> str1
'abc\ndefn'
>>> print(str1)
abc
defn
>>> name = input('What\'s your name: ')
What's your name: अनमोल राज 
>>> name
'अनमोल राज '
>>> #multi-lingual support (internationalization)name = input('What\'s your name: ')
>>> name = input('What\'s your name: ')
What's your name: àßdfgrwë
>>> name
'àßdfgrwë'
>>> name.encode()
b'\xc3\xa0\xc3\x9fdfgrw\xc3\xab'
>>> name2 = name.encode()
>>> type(name2)
<class 'bytes'>
>>> name2
b'\xc3\xa0\xc3\x9fdfgrw\xc3\xab'
>>> name2.decode()
'àßdfgrwë'
>>> str1 = 'python is a programming lang'
>>> str1.replace('python', 'java')
'java is a programming lang'
>>> str1.maketrans('pyti', 'xzam')
{112: 120, 121: 122, 116: 97, 105: 109}
>>> table = str1.maketrans('pyti', 'xzam')
>>> str1.translate(table)
'xzahon ms a xrogrammmng lang'
>>> table = str1.maketrans('pyti', 'xzam', 'l')
>>> str1.translate(table)
'xzahon ms a xrogrammmng ang'
>>> #what to replace, what characters to put in place, what characters to delete
>>> a = 10
>>> b = 20
>>> print(f"Value of {a} and {b}")
Value of 10 and 20
>>> print("{}{}{}".format_map(dict1)
