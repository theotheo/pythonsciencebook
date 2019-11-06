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

### немного магии

```python
%load_ext rpy2.ipython
```

# Базовые типы

| Тип | Пример |
|----|---|
| int  | 10 |
| float  | 10.1 |
| str  | "число" |
| bool  | True |
| NoneType  | None |


### int (integer; a whole number with no decimal place)

```R
10
-3
```

```python
10
-3
```


### float (float; a number that has a decimal place)
   

```R
7.41
```

```python
7.41
-0.006
```


### str (string; a sequence of characters enclosed in single quotes, double quotes, or triple quotes)

```R
'строка в одинарных кавычек'
"строка в двойных кавычках"
"строка в двойных кавычках со 'строкой из одинарных'"
'строка из одинарных кавычек с "строкой из двойных"'
```

```python
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
```

### bool (boolean; a binary value that is either true or false)

```R
TRUE
FALSE
T 
F
```

```python
True
False
```

### NoneType (a special type representing the absence of a value)

```R
NULL
```

```python
None
```

### type

```python
type(10)
```

```python
type(10.1)
```

```python
type('1')
```

### преобразование типов

```python
int(10.1)
int('10')
float('10.11')
str(10)
bool(10)
bool(0)
```

```python
float('11 тысяч')
```

```python
oct(10)
hex(10)
```

неявные преобразования типов (в условиях, логических операторах, при выводе)


## print

```R
print(10)
```

```python
print(10)
print('{}'.format(10))
```

## Операторы


### арифметические

| Symbol | Task Performed |
|----|---|
| +  | Addition |
| -  | Subtraction |
| /  | division |
| %  | mod |
| *  | multiplication |
| //  | floor division |
| **  | to the power of |

```R
print(2 + 2) 
print(2 / 3)
print(2 * 8)
```

```python
print(2 + 2)
print(2 / 3)
print(2 * 8)
```

```python
2 * 2 + 3
```

### операторы отношений

| Symbol | Task Performed |
|----|---|
| == | True, if it is equal |
| !=  | True, if not equal to |
| < | less than |
| > | greater than |
| <=  | less than or equal to |
| >=  | greater than or equal to |

```R
1 > 3
```

```python
1 > 3
```

### логические 

| Symbol | Task Performed |
|----|---|
| &  | Logical And |
| l  | Logical OR |
| ^  | XOR |
| ~  | Negate |
| >>  | Right shift |
| <<  | Left shift |

```R
1 | 0
```

```R
bitwShiftL(1, 2)
```

```python
1 | 0
1 << 2
```

```python
bin(1)
bin(2)
bin(4)
```

### Math

```R
v <- c(1, 3, 5)
round(3.13)
sum(v)
sd(v)
mean(v)
median(v)
```

```python
import math
import numpy as np

v = [1, 3, 5]
round(3.13)
sum(v)
np.std(v)
np.mean(v)
np.median(v)
```

## Переменные

```R
a <- 1
b <- 'one'
c <- c(1, 2, 3)
```

```R
c
```

```python
a = 1
b = 'one'
c = [1, 2, 3]
```

```python
c
```

### именование

имена переменных могут состоять из
- букв
- цифр
- знака подчеркивания

но начинаться только с букв и подчеркивания

```python
abc1 = 1
_abc1 = 1
```


```python
ab.c = 1
```

```python
1_abc = 1
```

```python
break = 1
```

### 30+ keywords

```python
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
```

```python
from IPython.display import HTML
HTML('https://martinfowler.com/bliki/TwoHardThings.html')
```

```python
%load_ext rpy2.ipython
```

# control structures


### if

```python
if (1):
    print(1)
```

```R
if (1) {
    print(1)
}
```

### for

```python cell_style="split"
lst = [1, 2, 3]

for el in lst:
    print(el)
```

```R cell_style="split"

lst <- c(1, 2, 3)
for (el in lst) {
    print(el)
}
```

### while

```python cell_style="split"
i = 0
while i < 10:
    i = i + 1
    print(i)
```

```R
i <- 0
while (i < 10) {
    i <- i + 1
    print(i)
}
```

### repeat

```python
####
```

## functions

```python
def foo(i):
    print(i)
    
foo(1)
```

```R
foo <- function(i) 
{
  print(i)
}

foo(1)


## Пакеты

### Установка
```

```bash
pip install pandas
```

```R
install.packages('dplyr')
```

### Импортирование

```R
library('dplyr')
```

```python
import pandas 
```

## Working directory

```R
curdir <- getwd()
print(curdir)
setwd('/tmp')
print(getwd())
setwd(curdir)
```

```python
import os
curdir = os.getcwd()
print(curdir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(curdir)
```

## DataFrames

```R
df <- data.frame(face = c("ace", "two", "six"),
    suit = c("clubs", "clubs", "clubs"), value = c(1, 2, 3)) 
df
```

```R
df[1]
```

```python
import pandas as pd

df = pd.DataFrame([['ace', 'two', 'six'], ['clubs', 'clubs', 'clubs'], [1, 2, 3]], 
             columns=['face', 'suit', 'value'])
df
```

```python
df.iloc[0]
```

    rpy2 is an interface to R running embedded in a Python process, and also includes functionality to deal with pandas DataFrames
https://pandas.pydata.org/pandas-docs/stable/r_interface.html


### pandas2ri

```python
from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import data
from rpy2.robjects.packages import importr

r.data('iris')
```

```python
r['iris'].head()
```

```python
datasets = importr('datasets')
mtcars_env = data(datasets).fetch('mtcars')
mtcars = mtcars_env['mtcars']

# austres
```

```python
py_mtcars = pandas2ri.ri2py(mtcars)
py_mtcars
```


```python
pandas2ri.py2ri(mtcars)
```

## importr


### ggplot

```python
datasets = importr('datasets')
# mtcars_env = data(datasets).fetch('austres')
# mtcars = mtcars_env['austres']
mtcars
```


```python
%matplotlib inline
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
```

```python
# ggplot() 
# + geom_line(data = jul1, aes(x = dday, y = clean_sum, colour = "Counts")) 
# + geom_line(data = jul1, aes(x = dday, y = cnt_ma, colour = "Weekly Moving Average")) 
```

### ddplyr

```python
from rpy2.robjects.lib.dplyr import DataFrame

dataf = (DataFrame(mtcars).
         filter('gear>3').
         mutate(powertoweight='hp*36/wt').
         group_by('gear').
         summarize(mean_ptw='mean(powertoweight)'))

dataf

```

```python
import rpy2.ipython.html
rpy2.ipython.html.init_printing()
```

```python
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
```

### foreign

```python
foreign = importr('foreign')
# pandas2ri.activateb
```

```python
lst = foreign.read_spss('data/international.sav', use_value_labels=True, to_data_frame=True)
lst
```

```python
list(lst[4][:5])
```
