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
#
#
#
#
#
#
#
#
#

# ## Working directory

import os
curdir = os.getcwd()
print(curdir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curdir)
#
#
