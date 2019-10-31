# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
    formats: ipynb//ipynb,md//md,py//py
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<div class="alert alert-block alert-info">Сколько бы преподаватель не знал и не понимал, он зачастую не знает важного -- сколько знает и что понимает его студент!</div>
 <div style="text-align: right"> Ильдар </div>


# Введение в Питон


## Читаем между строк


> Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

https://docs.python.org/3/tutorial/index.html


![](https://upload.wikimedia.org/wikipedia/en/c/cb/Flyingcircus_2.jpg)


- Python (https://en.wikipedia.org/wiki/Monty_Python)
- easy to learn (https://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext)
- powerful 
- programming 
- language (https://docs.python.org/3/reference/grammar.html)
- efficient high-level data structures 
- simple but effective approach to object-oriented programming
- elegant syntax (https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(syntax))
- dynamic typing 
- interpreted nature
- scripting
- rapid application development
- many areas
- most platforms


> The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

> The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

https://docs.python.org/3/tutorial/index.html


- extensive standard library (https://docs.python.org/3/library/index.html)
- freely available in source or binary (https://github.com/python/cpython)
- for all major platforms
- freely distributed
- many free third party Python modules (https://pypi.python.org/pypi)
- programs and tools, and additional documentation
- easily extended with new functions and data types
- also suitable as an extension language for customizable applications 


## Установка. Дистрибутивы. Библиотеки




## Интерпретатор and hello world

![](images/prompt.png)

 <div style="text-align: right"> за скриншот спасибо Нике Глазуновой </div> 


```
print("hello world!") 
```


python C:/Users/Ksenia/hello.py
python ".../hello py.txt"


<!-- #region -->
## Какой символ встречается чаще всего в приведенном коде?

```
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

solid = IN[0]
seed = IN[1]
xCount = IN[2]
yCount = IN[3]

solids = []

yDist = solid.BoundingBox.MaxPoint.Y-solid.BoundingBox.MinPoint.Y
xDist = solid.BoundingBox.MaxPoint.X-solid.BoundingBox.MinPoint.X

for i in xRange:
    for j in yRange:
        fromCoord = solid.ContextCoordinateSystem
        toCoord = fromCoord.Rotate(solid.ContextCoordinateSystem.Origin,Vector.ByCoordinates(0,0,1),(90*(i+j%val)))
        vec = Vector.ByCoordinates((xDist*i),(yDist*j),0)
        toCoord = toCoord.Translate(vec)
        solids.append(solid.Transform(fromCoord,toCoord))

OUT = solids```
<!-- #endregion -->

```python
code = """import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

solid = IN[0]
seed = IN[1]
xCount = IN[2]
yCount = IN[3]

solids = []

yDist = solid.BoundingBox.MaxPoint.Y-solid.BoundingBox.MinPoint.Y
xDist = solid.BoundingBox.MaxPoint.X-solid.BoundingBox.MinPoint.X

for i in xRange:
    for j in yRange:
        fromCoord = solid.ContextCoordinateSystem
        toCoord = fromCoord.Rotate(solid.ContextCoordinateSystem.Origin,Vector.ByCoordinates(0,0,1),(90*(i+j%val)))
        vec = Vector.ByCoordinates((xDist*i),(yDist*j),0)
        toCoord = toCoord.Translate(vec)
        solids.append(solid.Transform(fromCoord,toCoord))

OUT = solids"""

from collections import Counter
Counter([char for char in code]).most_common()
```











## Working directory

```python
import os
curdir = os.getcwd()
print(curdir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curdir)
```


# Reflections


## type 

```python
type(3)
```

```python
type(1.0)
```

```python
type(1 + 1j)
```

```python
type('Hello') 
```

```python
type([1, 2])
```

```python
type([1, [2, 'Hello']]) 
```

```python
type({'city': 'Paris'}) 
```

```python
type((1,2)) 
```

```python
type(set()) 
```

## Isinstance

```python
isinstance(3, int)
```

```python
isinstance([1, 2], list)
```

```python
isinstance(3, object)
```

```python
isinstance([1, 2], object)
```

```python
class Parent: pass                   
Parent
```

```python
class Child(Parent): pass   
Child
```

```python
child = Child()                           
```

```python
print isinstance(child, Child)    
```

```python
print isinstance(child, Parent) 
```

```python
print isinstance(child, object) 
```

## issubclass

```python
issubclass(Child, Parent)
```

```python
issubclass(Parent, Child)    
```

```python
issubclass(Child, object)    
```

```python
issubclass(Parent, object)    
```

## dir

```python
dir(1)
```

```python
dir('string')
```

## getattr

```python
getattr(3, "imag")
```

```python
f = getattr('string', 'upper')
f
```

```python
f()
```

## callable

```python
callable(2)
```

```python
callable(len)
```

```python
def foo():
    pass
callable(foo)
```

## keyword

```python
import keyword
pykeywords = keyword.kwlist
keyword.iskeyword("if")
keyword.iskeyword("True")
```

## __builtins__

```python
dir(__builtins__)  
```

# Exceptions


## Examples

```python
10 / 0
```

```python
prin(10)
```

```python
for i in [1, 2]
    print(i)
```

## Handling Exceptions

```python
try:
    10 / 0
except Exception:
    print('Exception')
```

```python
try:
    10 / 0
except Exception as e:
    print('Exception: {}'.format(e))
```

```python
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print( "Oops!  That was no valid number.  Try again...")
```

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print( "I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError:
    print( "Could not convert data to an integer.")
except:
    print( "Unexpected error:", sys.exc_info()[0])
    raise
```

## Built-in exceptions

```
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StopAsyncIteration
+-- ArithmeticError
| +-- FloatingPointError
| +-- OverflowError
| +-- ZeroDivisionError
+-- AssertionError
+-- AttributeError
+-- BufferError
+-- EOFError
+-- ImportError
+-- ModuleNotFoundError
+-- LookupError
| +-- IndexError
| +-- KeyError
+-- MemoryError
+-- NameError
| +-- UnboundLocalError
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
| +-- NotADirectoryError
| +-- PermissionError
| +-- ProcessLookupError
| +-- TimeoutError
+-- ReferenceError
+-- RuntimeError
| +-- NotImplementedError
| +-- RecursionError
+-- SyntaxError
| +-- IndentationError
| +-- TabError
+-- SystemError
+-- TypeError
+-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
+-- ResourceWarning
```

```python
from IPython.display import HTML
HTML('<iframe src="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" width=600 height=600>')
```

## Raise

```python
raise NameError('HiThere')
```

## finally

```python
i = 1

try:
    print(10 / i)
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('Goodbye, world!')
```

## User-defined exceptions

```python
def validate(name):
    if len(name) < 10:
        raise ValueError
```

```python
validate('joe')
```

```python
class NameTooShortError(ValueError):
    pass
```

```python
def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
##
```
