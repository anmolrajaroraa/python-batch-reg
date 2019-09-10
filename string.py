Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "python is a programming language"
>>> len(str1)
32
>>> str1[10]
'a'
>>> str1[20]
'i'
>>> str1[30]
'g'
>>> str1[31]
'e'
>>> str1[32]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str1[32]
IndexError: string index out of range
>>> str1[:5]
'pytho'
>>> str1[0:5]
'pytho'
>>> str1[0:15]
'python is a pro'
>>> str1[0:25]
'python is a programming l'
>>> #str1[starting_index : ending_index]  ,, ending_index_character will not be printed
>>> str1[:6]
'python'
>>> str1[:]
'python is a programming language'
>>> str1[0:31]
'python is a programming languag'
>>> str1[:]
'python is a programming language'
>>> str1[ : ]
'python is a programming language'
>>> str1[20]
'i'
>>> str1[24]
'l'
>>> str1[24:31]
'languag'
>>> str1[24:32]
'language'
>>> str1[32]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str1[32]
IndexError: string index out of range
>>> str1[24:33]
'language'
>>> str1[24:34]
'language'
>>> str1[24:35]
'language'
>>> str1[24:100]
'language'
>>> str1[100]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    str1[100]
IndexError: string index out of range
>>> str1[100:200]
''
>>> #if we directly write a wrong index, there will be an error
>>> str1[100]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    str1[100]
IndexError: string index out of range
>>> #if we are slicing, and we are giving some wrong indexes then there will be no errors, python will accordingly print the characters lying in that particular range
>>> str1[10:20]
'a programm'
>>> str1[10:40]
'a programming language'
>>> str1[35:40]
''
>>> str1[35:'40']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    str1[35:'40']
TypeError: slice indices must be integers or None or have an __index__ method
>>> str1[30:20]
''
>>> str1[30:20:1]
''
>>> #in slicing - > [start, end, step]
>>> str1[30:20:-1]
'gaugnal gn'
>>> str1[10:5:-1]
'a si '
>>> str1 = "python is a programming language"
>>> str1[10:3:-1]
'a si no'
>>> str1[10:0:-1]
'a si nohty'
>>> str1[10::-1]
'a si nohtyp'
>>> str1[10:-1:-1]
''
>>> str1[-1]
'e'
>>> str1[-2]
'g'
>>> str1[-3]
'a'
>>> str1[10:0:-1]
'a si nohty'
>>> str1[10:-1:-1]
''
>>> str1[10:-1:1]
'a programming languag'
>>> str1[10:0:1]
''
>>> str1[10:-2:1]
'a programming langua'
>>> str1[10:]
'a programming language'
>>> str1[10:100]
'a programming language'
>>> str1[10:]
'a programming language'
>>> str1[10::-1]
'a si nohtyp'
>>> #normally string index starts with 0
>>> #but in reverse, string index starts with -1
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> tuple
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

help> str
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> str1 = 'python'
>>> str1 = str('python')
>>> type(str1)
<class 'str'>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = 'python is a programming language'
>>> str1.capitalize()
'Python is a programming language'
>>> str1.casefold
<built-in method casefold of str object at 0x10e3bbfa8>
>>> str1.casefold()
'python is a programming language'
>>> str1 = 'python is a programming lAnguAge'
>>> str1.casefold()
'python is a programming language'
>>> str1.center()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    str1.center()
TypeError: center() takes at least 1 argument (0 given)
>>> str1.center(100)
'                                  python is a programming lAnguAge                                  '
>>> print(str1.center(100))
                                  python is a programming lAnguAge                                  
>>> print(str1.center(200))
                                                                                    python is a programming lAnguAge                                                                                    
>>> str1.center(200)
'                                                                                    python is a programming lAnguAge                                                                                    '
>>> str1.center(50)
'         python is a programming lAnguAge         '
>>> str2 = str1.center(50)
>>> len(str2)
50
>>> str1.center(100, fillchar='$')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    str1.center(100, fillchar='$')
TypeError: center() takes no keyword arguments
>>> str1.center(100, fillchar='  ')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    str1.center(100, fillchar='  ')
TypeError: center() takes no keyword arguments
>>> str1.center(width=100, fillchar='$')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str1.center(width=100, fillchar='$')
TypeError: center() takes no keyword arguments
>>> str1.center(width=100, fillchar='a')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    str1.center(width=100, fillchar='a')
TypeError: center() takes no keyword arguments
>>> str1.center(100, '$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$python is a programming lAnguAge$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> str1
'python is a programming lAnguAge'
>>> str1.count('a')
2
>>> str1.count('A')
2
>>> str1 = 'python is a programming language'
>>> str1.count('a')
4
>>> str1.count('is')
1
>>> str1.count('i')
2
>>> str1.count('s')
1
>>> str1.encode()
b'python is a programming language'
>>> b = str1.encode()
>>> b
b'python is a programming language'
>>> type(b)
<class 'bytes'>
>>> b.encode()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    b.encode()
AttributeError: 'bytes' object has no attribute 'encode'
>>> b.decode()
'python is a programming language'
>>> len(b)
32
>>> b = str1.encode('utf-8')
>>> b
b'python is a programming language'
>>> str2 = '%$#%&*('
>>> str2.encode()
b'%$#%&*('
>>> str2.encode('utf-8')
b'%$#%&*('
>>> str1.endswith('language')
True
>>> str1.endswith('lane')
False
>>> str1.endswith('programming')
False
>>> str1='python\tlanguage'
>>> str1
'python\tlanguage'
>>> str1.expandtabs()
'python  language'
>>> str1.expandtabs(10)
'python    language'
>>> print(str1)
python	language
>>> str1 = 'python\nlanguage'
>>> str1
'python\nlanguage'
>>> print(str1)
python
language
>>> str1='python\tlanguage'
>>> print(str1.expandtabs(tabsize=50))
python                                            language
>>> print(str1)
python	language
>>> print(str1.expandtabs())
python  language
>>> print(str1.expandtabs(100))
python                                                                                              language
>>> str1 = 'python is a programming language'
>>> str1.count('a')
4
>>> str1.find('a')
10
>>> str1.find('a',0)
10
>>> str1.find('a',10)
10
>>> str1.find('a',11)
17
>>> str1.find('a',18)
25
>>> str1.find('a',26)
29
>>> str1.index('a')
10
>>> str1.index('a',11)
17
>>> str1.index('ab',11)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    str1.index('ab',11)
ValueError: substring not found
>>> str1.find('ab',26)
-1
>>> str1.index('is',11)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    str1.index('is',11)
ValueError: substring not found
>>> str1.find('is')
7
>>> str1.index('is')
7
>>> str1.index('isa')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    str1.index('isa')
ValueError: substring not found
>>> str1.find('@')
-1
>>> str1.isalnum()
False
>>> str2 = 'abcd1234'
>>> str2.isalnum()
True
>>> str2.isalpha()
False
>>> str1.isalpha()
False
>>> str1
'python is a programming language'
>>> str3 = 'a'
>>> str3.isalpha()
True
>>> 'x'.isalpha()
True
>>> '1'.isalpha()
False
>>> 'æ'.isascii()
False
>>> 's'.isascii()
True
>>> '$'.isascii()
True
>>> '@'.isascii()
True
>>> str1.isascii()
True
>>> str3 = 'abcdæ'
>>> str3.isascii()
False
>>> str1 = 'python'
>>> str1.isalpha()
True
>>> str1 = 'python '
>>> str1.isalpha()
False
>>> str1 = 'python is a programming language'
>>> str1.strip()
'python is a programming language'
>>> str1.strip(' ')
'python is a programming language'
>>> print(str1.strip())
python is a programming language
>>> str1.replace(' ', '')
'pythonisaprogramminglanguage'
>>> new = str1.replace(' ', '')
>>> new
'pythonisaprogramminglanguage'
>>> new.isalpha()
True
>>> str5 = '    wfllkmbdbb      '
>>> str5.strip()
'wfllkmbdbb'
>>> str6 = '123445'
>>> str6.isdecimal()
True
>>> str6 = '123445abcd'
>>> str6.isdecimal()
False
>>> 'str6'.isidentifier()
True
>>> 'str7'.isidentifier()
True
>>> 'str8'.isidentifier()
True
>>> 'str_8'.isidentifier()
True
>>> '_str_8'.isidentifier()
True
>>> '$_str_8'.isidentifier()
False
>>> str8 = 'svsv'
>>> $str8 = 'geb'
SyntaxError: invalid syntax
>>> str6.isdigit()
False
>>> str5.isdigit()
False
>>> '1'.isdigit()
True
>>> '11'.isdigit()
True
>>> '11234'.isdigit()
True
>>> '1123467'.isdigit()
True
>>> str1
'python is a programming language'
>>> str1.replace(' ', '').isalpha()
True
>>> str1
'python is a programming language'
>>> str1 str1.replace(' ', '').isalpha()
SyntaxError: invalid syntax
>>> str1 = str1.replace(' ', '')
>>> str1
'pythonisaprogramminglanguage'
>>> str1.islower()
True
>>> str1.isnumeric()
False
>>> '1123467'.isnumeric()
True
>>> str1 = 'python is a programming language'
>>> str1.titlecase()
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    str1.titlecase()
AttributeError: 'str' object has no attribute 'titlecase'
>>> str1.title()
'Python Is A Programming Language'
>>> str1.title().istitle()
True
>>> str1.istitle()
False
>>> str1.join('abcd')
'apython is a programming languagebpython is a programming languagecpython is a programming languaged'
>>> str1.join(['abcd'])
'abcd'
>>> str1.join(str2)
'apython is a programming languagebpython is a programming languagecpython is a programming languagedpython is a programming language1python is a programming language2python is a programming language3python is a programming language4'
>>> '.'.join(str1,str2)
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    '.'.join(str1,str2)
TypeError: join() takes exactly one argument (2 given)
>>> '.'.join([str1,str2])
'python is a programming language.abcd1234'
>>> ' --- '.join(['python','functional programming'])
'python --- functional programming'
>>> str1
'python is a programming language'
>>> str1.find('a')
10
>>> str1.rfind('a')
29
>>> str1.rfind('a',28)
29
>>> str1.replace('python', 'java')
'java is a programming language'
>>> str1.split()
['python', 'is', 'a', 'programming', 'language']
>>> str1 = 'python_is_a_programming_language'
>>> str1.split('_')
['python', 'is', 'a', 'programming', 'language']
>>> str1.splitlines()
['python_is_a_programming_language']
>>> str1 = 'python_is_a_programming_language. lksvnslkvnslvksklvnsns. vksnvklsnvslvm'
>>> str1.splitlines()
['python_is_a_programming_language. lksvnslkvnslvksklvnsns. vksnvklsnvslvm']
>>> str1 = '''
lkavnlksnvlnsvs.sm.msm
svs ssdfdbdbdbdb
bdbdbbbbdbdbdb
'''
>>> str2 = 'ancdcd
SyntaxError: EOL while scanning string literal
>>> str1.splitlines()
['', 'lkavnlksnvlnsvs.sm.msm', 'svs ssdfdbdbdbdb', 'bdbdbbbbdbdbdb']
>>> str10 = '12'
>>> str10.zfill(10)
'0000000012'
>>> str1.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> print(str1.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> print(str1.__dir__)
<built-in method __dir__ of str object at 0x10e3c08f0>
>>> print(str1.__dir__())
['__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__mod__', '__rmod__', '__len__', '__getitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__new__', 'encode', 'replace', 'split', 'rsplit', 'join', 'capitalize', 'casefold', 'title', 'center', 'count', 'expandtabs', 'find', 'partition', 'index', 'ljust', 'lower', 'lstrip', 'rfind', 'rindex', 'rjust', 'rstrip', 'rpartition', 'splitlines', 'strip', 'swapcase', 'translate', 'upper', 'startswith', 'endswith', 'isascii', 'islower', 'isupper', 'istitle', 'isspace', 'isdecimal', 'isdigit', 'isnumeric', 'isalpha', 'isalnum', 'isidentifier', 'isprintable', 'zfill', 'format', 'format_map', '__format__', 'maketrans', '__sizeof__', '__getnewargs__', '__doc__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__dir__', '__class__']
>>> 
