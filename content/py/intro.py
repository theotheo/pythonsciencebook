# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb//ipynb,md//md,py//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# <div class="alert alert-block alert-info">Сколько бы преподаватель не знал и не понимал, он зачастую не знает важного -- сколько знает и что понимает его студент!</div>
#  <div style="text-align: right"> Ильдар </div>

# # Введение в Питон

# ## Читаем между строк

# > Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
#
# https://docs.python.org/3/tutorial/index.html

# ![](https://upload.wikimedia.org/wikipedia/en/c/cb/Flyingcircus_2.jpg)

# - Python (https://en.wikipedia.org/wiki/Monty_Python)
# - easy to learn (https://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext)
# - powerful 
# - programming 
# - language (https://docs.python.org/3/reference/grammar.html)
# - efficient high-level data structures 
# - simple but effective approach to object-oriented programming
# - elegant syntax (https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(syntax))
# - dynamic typing 
# - interpreted nature
# - scripting
# - rapid application development
# - many areas
# - most platforms

# > The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
#
# > The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.
#
# https://docs.python.org/3/tutorial/index.html

# - extensive standard library (https://docs.python.org/3/library/index.html)
# - freely available in source or binary (https://github.com/python/cpython)
# - for all major platforms
# - freely distributed
# - many free third party Python modules (https://pypi.python.org/pypi)
# - programs and tools, and additional documentation
# - easily extended with new functions and data types
# - also suitable as an extension language for customizable applications 

# ## Установка. Дистрибутивы. Библиотеки
#
#

# ## Интерпретатор and hello world
#
# ![](images/prompt.png)
#
#  <div style="text-align: right"> за скриншот спасибо Нике Глазуновой </div> 
#

# + {"active": ""}
# print("hello world!") 
# -


# python C:/Users/Ksenia/hello.py
# python ".../hello py.txt"
#

# ## Какой символ встречается чаще всего в приведенном коде?
#
# ```
# import clr
# clr.AddReference('ProtoGeometry')
# from Autodesk.DesignScript.Geometry import *
#
# solid = IN[0]
# seed = IN[1]
# xCount = IN[2]
# yCount = IN[3]
#
# solids = []
#
# yDist = solid.BoundingBox.MaxPoint.Y-solid.BoundingBox.MinPoint.Y
# xDist = solid.BoundingBox.MaxPoint.X-solid.BoundingBox.MinPoint.X
#
# for i in xRange:
#     for j in yRange:
#         fromCoord = solid.ContextCoordinateSystem
#         toCoord = fromCoord.Rotate(solid.ContextCoordinateSystem.Origin,Vector.ByCoordinates(0,0,1),(90*(i+j%val)))
#         vec = Vector.ByCoordinates((xDist*i),(yDist*j),0)
#         toCoord = toCoord.Translate(vec)
#         solids.append(solid.Transform(fromCoord,toCoord))
#
# OUT = solids```

# +
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
# -


# ## Базовые типы
#

# ### int (integer; целое число; целочисленный тип)

10

-3

0x10

0b10111

# ### float (float; число с плавающей запятой)
#    

7.41

-0.006

0.1

.2

2e10

2 * 10**10

2**10

# ### str (string; строка; последовательность заключенная в кавычки)

'строка в одинарных кавычек'

"строка в двойных кавычках"

"строка в двойных кавычках со 'строкой из одинарных'"

'строка из одинарных кавычек с "строкой из двойных"'

"""sun
shine"""

"su"

'''строка в трех одинарных кавычек'''

"""строка в трех двойных кавычках"""
"""'одинарные кавычки' в строке с "двойными" в трех двойных"""
"""
тройных
кавычки
мультистроковы
"""

# ### bool (boolean; бинарные значения)

True

False

True
False

# ### NoneType (a special type representing the absence of a value)

None

# ### базовые типы и их "литеральный"синтаксис

# | Тип | Пример |
# |----|---|
# | int  | 10, 0x10 |
# | float  | 10.1, 2e10 |
# | str  | "число", """еще одна строка""" |
# | bool  | True, False |
# | NoneType  | None |

# ## Вызов функции

help

help()

# ## Функция type

type(10)

type(10.1)

type('1')

type("""1""")

# ## Преобразование типов из одного в другой

int(10.1)

type(int('10'))

float('10.11')

str(10)

bool(10)

bool(0)

float('11 тысяч')

0o20

oct(10)

hex(10)

# неявные преобразования типов (в условиях, логических операторах, при выводе)

# ## print

print(10)

print(5.5)

print('строка')

print(True)

# ## интерполяция строк

s = 'в аудитории сейчас' + ' ' + 'жарко'
print(s)

s = 'за окном сейчас - {}'.format(8) 
print(s)

s = 'за окном скоро +%d' % 20 
print(s)



# ## Всё -- объект

# ![](http://forum.ostmetal.info/data/attachments/96/96957-a0bd7a2c1812e60b472436b9ce51995b.jpg)

# ![](http://mama66.ru/wp-content/uploads/sdelat_pesochnicu_1.jpg)

(2).__add__(6)

# ### Функция dir -- что лежит в объекте

dir(2)

# ### Операции с объектами

(2).__bool__()

(2).__mul__(10)

'строка'.__add__('еще строка')

'строка'.__mul__(3)

# ## Операторы

# ### арифметические
#
# | Символ | Что делает |
# |----|---|
# | +  | Сложение |
# | -  | Вычитание |
# | /  | Деление |
# | %  | Модуль числа |
# | *  | Умножение |
# | //  | Целочисленное деление |
# | **  | Возведение в степень |

print(2 + 2)

print(2 / 3)

print(2 * 8)

2 * 2 + 3

2 * (2 + 3)

# ### операторы отношений
#
# | Символ | Что делает |
# |----|---|
# | == | True, если эквиваленты |
# | !=  | True, если не эквивалентны |
# | < | меньше чем |
# | > | больше чем |
# | <=  | меньше или равно |
# | >=  | больше или равно |

1 > 3

'fdf' > 'fdfdfd'

'fdf' < 'fdfdfd'

'fdf' == 'fdf'

'fdf' == 'abc'

# ### битовые 
#
# | Символ | Что делает |
# |----|---|
# | &  | И |
# | l  | Или |
# | ^  | XOR (исключающее или) |
# | ~  | Отрицание |
# | >>  | Сдвиг вправо |
# | <<  | Сдвиг влево |

bin(1)
bin(2)
bin(4)

# ## Переменные -- это ярлыки

1 

a = 1

ulyanov = 1

lenin = 1

ulyanov

lenin + lenin

a = 2

a 

l = [1, 'fdfd', 2]

type(l)

a = 1
b = 'one'
c = [1, 2, 3]

c

d = c

d

c[1] = 'AAA'

c

d

f = c.copy()

f


c

c[0] = 10

c

id(c)

id(d)

c == d

(10).__add__(2)

f = c.copy()

f == c

id(f)

# ### именование
#
# имена переменных могут состоять из
# - букв
# - цифр
# - знака подчеркивания
#
# но начинаться только с букв и подчеркивания

abc1 = 1
_abc1 = 1


ab.c = 1

1_abc = 1

break = 1

# ### 30+ keywords

and
as 
assert 
break 
class 
continue
def
del 
elif 
else 
except 
exec
finally 
for 
from 
global 
if 
import
in 
is 
lambda 
nonlocal 
not 
or
pass 
raise 
return 
try 
while 
with
yield 
True 
False 
None

from IPython.display import HTML
HTML('<iframe width=800 height=400 src="https://martinfowler.com/bliki/TwoHardThings.html">')


# ### underscore, dunders
#
# - одно подчеркивание в начале: _var
# - одно подчеркивание с конца: var_
# - двойное подчеркивание в начале: __var
# - двойное подчеркивание в начале и с конца: __var__
# - просто подчеркивание: _



# ## Sets

x = set([1, 2, 3])
type(x)

y = {2, 3, 5}
type(y)

# ### mutable

x.add(10)
x

# ### unordered

x[1]

# ### operations

# #### union

x.union(y) 

# #### intersection

x.intersection(y)

# #### difference

x - y

# ### vienna diagramm for fun

# ! pip install --user matplotlib-venn

from matplotlib_venn import venn2
# %matplotlib inline

venn2([x, y])

# ## enumerate

abc = ['a', 'c', 'd']
enumerate(abc)

for index, el  in enumerate(abc):
    print(index)


# ## Function first-class citizens
#
# Функции можно присваивать переменным, сохранять в структурах данных, передавать как аргументы другим функциям и возвращать как значение функций
#
# ### присвоение

def yell(text):
    return text.upper() + '!'


bark = yell # присваиваем

bark('woof')

del yell # удаляем

yell('hello?')

bark('hey')

bark.__name__ # имя для дебага

# ### сохраняем
# + {}
funcs = [bark, str.lower, str.capitalize]
funcs

for f in funcs:
    print(f, f('hey there'))

funcs[0]('heyho')


# -
# ### передаем в функцию

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)


def whisper(text):
    return text.lower() + '...'


greet(whisper)

# higher-order functions -- функции, которые принимают другие функции. например, `map`

list(map(bark, ['hello', 'hey', 'hi']))


# ### вложенные функции

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


speak('Hello, World')

whisper('Yo') # не существует


# ### можно вернуть функцию из функции
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


get_speak_func(0.3)
get_speak_func(0.7)
speak_func = get_speak_func(0.7)
speak_func('Hello')


# ### функции схватывают контекст

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


get_speak_func('Hello, World', 0.7)()


# Это называется (лексическое) *замыкание* (lexical closures)
#
# Можно конфигурировать поведение

# +
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

plus_3(4)
plus_5(4)


# -

# ### объекты могут вести себя как функции

# + {"": null, "python": null, "active": ""}
# class Adder:
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, x): # dunder метод
#         return self.n + x
#
# plus_3 = Adder(3)
# plus_3(4)
# -

# ### args, kwargs
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# +
foo()

foo('hello')

foo('hello', 1, 2, 3)

foo('hello', 1, 2, 3, key1='value', key2=999)
# -

# ### lambda -- безымянные функции

add = lambda x, y: x + y

add(5, 3)


# +
def add(x, y):
    return x + y

add(5, 3)
# -
# Лямбды ограничены одним выражением (expressions). Т.е нельзя использовать statements и таким образом даже `return`.
#
# Т.е. лямбда -- single expression function

sorted(range(-5, 6), key=lambda x: x * x)

list(filter(lambda x: x % 2 == 0, range(16))) # так не надо

[x for x in range(16) if x % 2 == 0] # лучше так


# ## decorators
# Декораторы -- оборачивают (wrap) другую функцию и позволяет выполнить какой-то код до или после нее. 
#
# ### "нулевой" декоратор

def null_decorator(func):
    return func


# +
def greet():
    return 'Hello!'

greet = null_decorator(greet)


# -

# > a decorator is a callable that takes a callable as input and returns another callable.
#
# ### @

@null_decorator
def greet():
    return 'Hello!'


greet()


# ### изменяем поведение
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
    def greet():
        return 'Hello!'

# +
greet

null_decorator(greet)

uppercase(greet)


# -

# ### множественное

# +
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


# +
@strong
@emphasis
def greet():
    return 'Hello!'

greet()
# -

decorated_greet = strong(emphasis(greet))

# ## List comprehensions
# https://www.python.org/dev/peps/pep-0279/

# ### list

sample = [1, 2, 3, 4] 

[a for a in sample if a % 2]

# ### set

{a*2 for a in sample}

# ### dict

{i:a for i, a in enumerate(sample) }

# ## nested

# +
my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)
        
my_list
# -

[x * y for x in [20, 40, 60] for y in [2, 4, 6]]


# ## Управляющие структуры

# ### if

1 == 0

# +
if (1 != 0):
    print(1)
    print(11)

print(10)

# -

if(2 > 3):
    print('2 > 3')
else:
    print('2 < 3')

from_user = 'F'
if (from_user == 'M'):
    print('введено M')
elif (from_user == 'F'):
    print('введено F')
elif (from_user == 'FM'):
    print('введено FM')
elif (from_user == ''):
    print('пустая строка')
else:
    print('что-то еще')

# ### for

food_orders = ['pizza', 'not pizza']

for food in food_orders:
    print(food.upper())

# +

for el in [1, 2, 3]:
    print(el)
# -

# ### while

i = 0
while i < 10:
    i = i + 1
    print(i)

4 % 2

bool(0)

i = 0
while True:
    i = i + 1
    if i % 2:
        continue
        
    print(i)
    if i > 9:
        break


# ## Функции -- их можно создавать
#
# ```
# def name(var):
#     """doc string"""
#     body
#     return stm
# ```
#
# ```
# my_var = name(obj)
# ```

# +
def foo(i, j):
    print(i*3)

foo(1, 2)
# -

# ## Пакеты

# ### Установка

# + {"language": "bash"}
# pip install jupyter
# -

jupyter notebook

# ### Импортирование

import pandas

# ## Working directory

import os
curdir = os.getcwd()
print(curdir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curdir)


# # Reflections

# ## type 

type(3)

type(1.0)

type(1 + 1j)

type('Hello') 

type([1, 2])

type([1, [2, 'Hello']]) 

type({'city': 'Paris'}) 

type((1,2)) 

type(set()) 

# ## Isinstance

isinstance(3, int)

isinstance([1, 2], list)

isinstance(3, object)

isinstance([1, 2], object)


class Parent: pass                   
Parent


class Child(Parent): pass   
Child

child = Child()                           

print isinstance(child, Child)    

print isinstance(child, Parent) 

print isinstance(child, object) 

# ## issubclass

issubclass(Child, Parent)

issubclass(Parent, Child)    

issubclass(Child, object)    

issubclass(Parent, object)    

# ## dir

dir(1)

dir('string')

# ## getattr

getattr(3, "imag")

f = getattr('string', 'upper')
f

f()

# ## callable

callable(2)

callable(len)


def foo():
    pass
callable(foo)

# ## keyword

import keyword
pykeywords = keyword.kwlist
keyword.iskeyword("if")
keyword.iskeyword("True")

# ## __builtins__

dir(__builtins__)  

# # Exceptions

# ## Examples

10 / 0

prin(10)

for i in [1, 2]
    print(i)

# ## Handling Exceptions

try:
    10 / 0
except Exception:
    print('Exception')

try:
    10 / 0
except Exception as e:
    print('Exception: {}'.format(e))

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print( "Oops!  That was no valid number.  Try again...")

# +
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
# -

# ## Built-in exceptions

# + {"active": ""}
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
# +-- StopIteration
# +-- StopAsyncIteration
# +-- ArithmeticError
# | +-- FloatingPointError
# | +-- OverflowError
# | +-- ZeroDivisionError
# +-- AssertionError
# +-- AttributeError
# +-- BufferError
# +-- EOFError
# +-- ImportError
# +-- ModuleNotFoundError
# +-- LookupError
# | +-- IndexError
# | +-- KeyError
# +-- MemoryError
# +-- NameError
# | +-- UnboundLocalError
# +-- OSError
# | +-- BlockingIOError
# | +-- ChildProcessError
# | +-- ConnectionError
# | | +-- BrokenPipeError
# | | +-- ConnectionAbortedError
# | | +-- ConnectionRefusedError
# | | +-- ConnectionResetError
# | +-- FileExistsError
# | +-- FileNotFoundError
# | +-- InterruptedError
# | +-- IsADirectoryError
# | +-- NotADirectoryError
# | +-- PermissionError
# | +-- ProcessLookupError
# | +-- TimeoutError
# +-- ReferenceError
# +-- RuntimeError
# | +-- NotImplementedError
# | +-- RecursionError
# +-- SyntaxError
# | +-- IndentationError
# | +-- TabError
# +-- SystemError
# +-- TypeError
# +-- ValueError
# | +-- UnicodeError
# | +-- UnicodeDecodeError
# | +-- UnicodeEncodeError
# | +-- UnicodeTranslateError
# +-- Warning
# +-- DeprecationWarning
# +-- PendingDeprecationWarning
# +-- RuntimeWarning
# +-- SyntaxWarning
# +-- UserWarning
# +-- FutureWarning
# +-- ImportWarning
# +-- UnicodeWarning
# +-- BytesWarning
# +-- ResourceWarning
# -

from IPython.display import HTML
HTML('<iframe src="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" width=600 height=600>')

# ## Raise

raise NameError('HiThere')

# ## finally

# +
i = 1

try:
    print(10 / i)
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('Goodbye, world!')


# -

# ## User-defined exceptions

def validate(name):
    if len(name) < 10:
        raise ValueError


validate('joe')


class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
##
