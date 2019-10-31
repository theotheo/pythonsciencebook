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

# ### немного магии

# %load_ext rpy2.ipython

# # Базовые типы
#
# | Тип | Пример |
# |----|---|
# | int  | 10 |
# | float  | 10.1 |
# | str  | "число" |
# | bool  | True |
# | NoneType  | None |

# ### int (integer; a whole number with no decimal place)

# + {"language": "R"}
# 10
# -3
# -

10
-3


# ### float (float; a number that has a decimal place)
#    

# + {"language": "R"}
# 7.41
# -

7.41
-0.006


# ### str (string; a sequence of characters enclosed in single quotes, double quotes, or triple quotes)

# + {"language": "R"}
# 'строка в одинарных кавычек'
# "строка в двойных кавычках"
# "строка в двойных кавычках со 'строкой из одинарных'"
# 'строка из одинарных кавычек с "строкой из двойных"'
# -

'строка в одинарных кавычек'
"строка в двойных кавычках"
"строка в двойных кавычках со 'строкой из одинарных'"
'строка из одинарных кавычек с "строкой из двойных"'
'''строка в трех одинарных кавычек'''
"""строка в трех двойных кавычках"""
"""'одинарные кавычки' в строке с "двойными" в трех двойных"""
"""
тройных
кавычки
мультистроковы
"""

# ### bool (boolean; a binary value that is either true or false)

# + {"language": "R"}
# TRUE
# FALSE
# T 
# F
# -

True
False

# ### NoneType (a special type representing the absence of a value)

# + {"language": "R"}
# NULL
# -

None

# ### type

type(10)

type(10.1)

type('1')

# ### преобразование типов

int(10.1)
int('10')
float('10.11')
str(10)
bool(10)
bool(0)

float('11 тысяч')

oct(10)
hex(10)

# неявные преобразования типов (в условиях, логических операторах, при выводе)

# ## print

# + {"language": "R"}
# print(10)
# -

print(10)
print('{}'.format(10))

# ## Операторы

# ### арифметические
#
# | Symbol | Task Performed |
# |----|---|
# | +  | Addition |
# | -  | Subtraction |
# | /  | division |
# | %  | mod |
# | *  | multiplication |
# | //  | floor division |
# | **  | to the power of |

# + {"language": "R"}
# print(2 + 2) 
# print(2 / 3)
# print(2 * 8)
# -

print(2 + 2)
print(2 / 3)
print(2 * 8)

2 * 2 + 3

# ### операторы отношений
#
# | Symbol | Task Performed |
# |----|---|
# | == | True, if it is equal |
# | !=  | True, if not equal to |
# | < | less than |
# | > | greater than |
# | <=  | less than or equal to |
# | >=  | greater than or equal to |

# + {"language": "R"}
# 1 > 3
# -

1 > 3

# ### логические 
#
# | Symbol | Task Performed |
# |----|---|
# | &  | Logical And |
# | l  | Logical OR |
# | ^  | XOR |
# | ~  | Negate |
# | >>  | Right shift |
# | <<  | Left shift |

# + {"language": "R"}
# 1 | 0

# + {"language": "R"}
# bitwShiftL(1, 2)
# -

1 | 0
1 << 2

bin(1)
bin(2)
bin(4)

# ### Math

# + {"language": "R"}
# v <- c(1, 3, 5)
# round(3.13)
# sum(v)
# sd(v)
# mean(v)
# median(v)

# +
import math
import numpy as np

v = [1, 3, 5]
round(3.13)
sum(v)
np.std(v)
np.mean(v)
np.median(v)
# -

# ## Переменные

# + {"language": "R"}
# a <- 1
# b <- 'one'
# c <- c(1, 2, 3)

# + {"language": "R"}
# c
# -

a = 1
b = 'one'
c = [1, 2, 3]

c

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
HTML('https://martinfowler.com/bliki/TwoHardThings.html')

# %load_ext rpy2.ipython

# # control structures

# ### if

if (1):
    print(1)

# + {"language": "R"}
# if (1) {
#     print(1)
# }
# -

# ### for

# + {"cell_style": "split"}
lst = [1, 2, 3]

for el in lst:
    print(el)

# + {"cell_style": "split", "language": "R"}
#
# lst <- c(1, 2, 3)
# for (el in lst) {
#     print(el)
# }
# -

# ### while

# + {"cell_style": "split"}
i = 0
while i < 10:
    i = i + 1
    print(i)


# + {"language": "R"}
# i <- 0
# while (i < 10) {
#     i <- i + 1
#     print(i)
# }
# -

# ### repeat

# +
####
# -

# ## functions

# +
def foo(i):
    print(i)
    
foo(1)

# + {"language": "R"}
# foo <- function(i) 
# {
#   print(i)
# }
#
# foo(1)
#
#
# ## Пакеты
#
# ### Установка

# + {"language": "bash"}
# pip install pandas

# + {"language": "R"}
# install.packages('dplyr')
# -

# ### Импортирование

# + {"language": "R"}
# library('dplyr')
# -

import pandas 

# ## Working directory

# + {"language": "R"}
# curdir <- getwd()
# print(curdir)
# setwd('/tmp')
# print(getwd())
# setwd(curdir)
# -

import os
curdir = os.getcwd()
print(curdir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curdir)

# ## DataFrames

# + {"language": "R"}
# df <- data.frame(face = c("ace", "two", "six"),
#     suit = c("clubs", "clubs", "clubs"), value = c(1, 2, 3)) 
# df

# + {"language": "R"}
# df[1]

# +
import pandas as pd

df = pd.DataFrame([['ace', 'two', 'six'], ['clubs', 'clubs', 'clubs'], [1, 2, 3]], 
             columns=['face', 'suit', 'value'])
df
# -

df.iloc[0]

#     rpy2 is an interface to R running embedded in a Python process, and also includes functionality to deal with pandas DataFrames
# https://pandas.pydata.org/pandas-docs/stable/r_interface.html

# ### pandas2ri

# +
from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import data
from rpy2.robjects.packages import importr

r.data('iris')
# -

r['iris'].head()

# +
datasets = importr('datasets')
mtcars_env = data(datasets).fetch('mtcars')
mtcars = mtcars_env['mtcars']

# austres
# -

py_mtcars = pandas2ri.ri2py(mtcars)
py_mtcars


pandas2ri.py2ri(mtcars)

# ## importr

# ### ggplot

datasets = importr('datasets')
# mtcars_env = data(datasets).fetch('austres')
# mtcars = mtcars_env['austres']
mtcars


# +
# %matplotlib inline
import numpy as np
import pandas as pd
import rpy2.robjects.packages as packages
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro

R = ro.r
gp = ggplot2.ggplot(mtcars)
pp = (gp 
      + ggplot2.aes_string(x='wt', y='mpg')
      + ggplot2.geom_point(ggplot2.aes_string(colour='qsec'))
      + ggplot2.scale_colour_gradient(low="yellow", high="red") 
      + ggplot2.geom_smooth(method='auto') 
      + ggplot2.labs(title="mtcars", x='wt', y='mpg'))
pp.plot()

# +
# ggplot() 
# # + geom_line(data = jul1, aes(x = dday, y = clean_sum, colour = "Counts")) 
# # + geom_line(data = jul1, aes(x = dday, y = cnt_ma, colour = "Weekly Moving Average")) 
# -

# ### ddplyr

# +
from rpy2.robjects.lib.dplyr import DataFrame

dataf = (DataFrame(mtcars).
         filter('gear>3').
         mutate(powertoweight='hp*36/wt').
         group_by('gear').
         summarize(mean_ptw='mean(powertoweight)'))

dataf

# -

import rpy2.ipython.html
rpy2.ipython.html.init_printing()

# +
from rpy2.robjects.lib.dplyr import (filter,
                                     mutate,
                                     group_by,
                                     summarize)

dataf = (DataFrame(mtcars) >>
         filter('gear>3') >>
         mutate(powertoweight='hp*36/wt') >>
         group_by('gear') >>
         summarize(mean_ptw='mean(powertoweight)'))

dataf
# -

# ### foreign

foreign = importr('foreign')
# pandas2ri.activateb

lst = foreign.read_spss('data/international.sav', use_value_labels=True, to_data_frame=True)
lst

list(lst[4][:5])
