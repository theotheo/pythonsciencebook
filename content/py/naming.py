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
