# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb//ipynb,py//py,md//md
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

#
# # Интроспекция и рефлексия
#
# В философии и психологии инстроспекцией называют акт самонаблюдения, в процессе которого происходит более глубокое познание себя и своей психики.  
#
# **Интроспекцией** (introspection) в computer science называют способность программы узнавать типы и свойства объектов во время выполнения. Так же существует термин **рефлексия** (reflection) развивающий идею интроспекции -- это уже способность программы менять свойства объектов.
#
# Интроспекция является важной частью Python и реализует в нем целым рядом способов.

# ## dir
#
# Пожалуй, самый полезный интроспективный метод. `dir` возвращает список того, что "содержится" в объекте: его функции и переменные. Или говоря корректнее, его методы и свойства. 

dir(1)

dir('string')

# Нельзя не обратить внимание, что в длинном перечне большая часть занимают имена вида `__xxxxx__`. Это так называемые специальные (special) или магические методы (magic), которые реализуют и на самом деле функционал операторов. Например, в методе `__add__` чисел и спрятан код, который работает при их сложении. Подробнее, о них мы поговорим в отдельной главе. А чтобы убедиться, что это так можно вызвав метод напрямую

2 + 2

(2).__add__(2) # первые скобки нужны, чтобы точка не посчиталось частью числа

# Есть еще один способ сделать то же самое -- без подробностей:

import operator
operator.add(2, 2)

# Так как все в Питоне является объектом, то можно посмотреть с помощью `dir` содержимое какого-нибудь модуля

import math
dir(math)

# Так же вероятно неожиданным является возможность посмотреть содержимое текущей области видимости: для этого надо вызвать `dir` без параметров.

dir()

# в Jupyter в текущей области видимости будет много переменных вида `_X`, где X -- это число.
#
# // TODO: пояснить 

# И другой интересный пример интроспекции с помощью `dir` -- это взгляд на содержимое `__builtins__`

dir(__builtins__)  

# ## type 
#
# `type` показывает класс объекта

type(3)

type(1.0)

type(1 + 1j)

type('Hello') 

type([1, 2])

type([1, [2, 'Hello']]) 

type({'city': 'Paris'}) 

type((1,2)) 

type(set()) 

type(math)

# ## Isinstance
#
# Проверяет является ли объект экземпляром данного класса (типа).  

isinstance(3, int)

isinstance([1, 2], list)

isinstance(3, object)

isinstance([1, 2], object)


# Надо понимать, что если у класса есть родители, то экземпляр данного класса так же является экземпляром класса родителя. Давайте посмотрим на примере.

class Parent: pass                   
Parent


class Child(Parent): pass   
Child

child = Child()                           

isinstance(child, Child)    

isinstance(child, Parent) 

# И, соответственно, так как все объекты в Python имеют своим прародителем класс `object`, то и любой объект является экземпляром этого класса 

isinstance(child, object) 

# ## issubclass
#
# Проверяет является ли один класс подклассом другого класса, то есть отнаследован ли один класс от другого.

issubclass(Child, Parent)

issubclass(Parent, Child)    

issubclass(Child, object)    

issubclass(Parent, object)    

# ## callable
#
# Показывает является ли объект callable, то есть вызываемым. Другими словами, можно ли вызвать данный объект как функцию.

callable(2)

callable(len)


# +
def foo():
    pass

callable(foo)
# -

# ## keyword
#
# Модуль `keyword` помогает понять какие слова являются зарезервированными

import keyword
print(keyword.kwlist)

len(keyword.kwlist)

keyword.iskeyword("if")

keyword.iskeyword("True")

keyword.iskeyword("foo")

# Источники и дополнительное чтение:
# - https://en.wikibooks.org/wiki/Python_Programming/Reflection
# - https://www.ibm.com/developerworks/library/l-pyint/index.html
