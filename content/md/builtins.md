# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
    formats: ipynb//ipynb,py//py,md//md
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


## Базовые типы



### int (integer; целое число; целочисленный тип)

```python
10
```

```python
-3
```

```python
0x10
```

```python
0b10111
```

### float (float; число с плавающей запятой)
   

```python
7.41
```

```python
-0.006
```

```python
0.1
```

```python
.2
```

```python
2e10
```

```python
2 * 10**10
```

```python
2**10
```

### str (string; строка; последовательность заключенная в кавычки)

```python
'строка в одинарных кавычек'
```

```python
"строка в двойных кавычках"
```

```python
"строка в двойных кавычках со 'строкой из одинарных'"
```

```python
'строка из одинарных кавычек с "строкой из двойных"'
```

```python
"""sun
shine"""
```

```python
"su"
```

```python
'''строка в трех одинарных кавычек'''
```

```python
"""строка в трех двойных кавычках"""
"""'одинарные кавычки' в строке с "двойными" в трех двойных"""
"""
тройных
кавычки
мультистроковы
"""
```

### bool (boolean; бинарные значения)

```python
True
```

```python
False
```

```python
True
False
```

### NoneType (a special type representing the absence of a value)

```python
None
```

### базовые типы и их "литеральный"синтаксис


| Тип | Пример |
|----|---|
| int  | 10, 0x10 |
| float  | 10.1, 2e10 |
| str  | "число", """еще одна строка""" |
| bool  | True, False |
| NoneType  | None |


## Вызов функции

```python
help
```

```python
help()
```

## Функция type

```python
type(10)
```

```python
type(10.1)
```

```python
type('1')
```

```python
type("""1""")
```

## Преобразование типов из одного в другой

```python
int(10.1)
```

```python
type(int('10'))
```

```python
float('10.11')
```

```python
str(10)
```

```python
bool(10)
```

```python
bool(0)
```

```python
float('11 тысяч')
```

```python
0o20
```

```python
oct(10)
```

```python
hex(10)
```

неявные преобразования типов (в условиях, логических операторах, при выводе)


## print

```python
print(10)
```

```python
print(5.5)
```

```python
print('строка')
```

```python
print(True)
```

## интерполяция строк

```python
s = 'в аудитории сейчас' + ' ' + 'жарко'
print(s)
```

```python
s = 'за окном сейчас - {}'.format(8) 
print(s)
```

```python
s = 'за окном скоро +%d' % 20 
print(s)
```

```python

```

## Всё -- объект


![](http://forum.ostmetal.info/data/attachments/96/96957-a0bd7a2c1812e60b472436b9ce51995b.jpg)


![](http://mama66.ru/wp-content/uploads/sdelat_pesochnicu_1.jpg)

```python
(2).__add__(6)
```

### Функция dir -- что лежит в объекте

```python
dir(2)
```

### Операции с объектами

```python
(2).__bool__()
```

```python
(2).__mul__(10)
```

```python
'строка'.__add__('еще строка')
```

```python
'строка'.__mul__(3)
```

## Операторы


### арифметические

| Символ | Что делает |
|----|---|
| +  | Сложение |
| -  | Вычитание |
| /  | Деление |
| %  | Модуль числа |
| *  | Умножение |
| //  | Целочисленное деление |
| **  | Возведение в степень |

```python
print(2 + 2)
```

```python
print(2 / 3)
```

```python
print(2 * 8)
```

```python
2 * 2 + 3
```

```python
2 * (2 + 3)
```

### операторы отношений

| Символ | Что делает |
|----|---|
| == | True, если эквиваленты |
| !=  | True, если не эквивалентны |
| < | меньше чем |
| > | больше чем |
| <=  | меньше или равно |
| >=  | больше или равно |

```python
1 > 3
```

```python
'fdf' > 'fdfdfd'
```

```python
'fdf' < 'fdfdfd'
```

```python
'fdf' == 'fdf'
```

```python
'fdf' == 'abc'
```

### битовые 

| Символ | Что делает |
|----|---|
| &  | И |
| l  | Или |
| ^  | XOR (исключающее или) |
| ~  | Отрицание |
| >>  | Сдвиг вправо |
| <<  | Сдвиг влево |

```python
bin(1)
bin(2)
bin(4)
```

## Переменные -- это ярлыки

```python
1 
```

```python
a = 1
```

```python
ulyanov = 1
```

```python
lenin = 1
```

```python
ulyanov
```

```python
lenin + lenin
```

```python
a = 2
```

```python
a 
```

```python
l = [1, 'fdfd', 2]
```

```python
type(l)
```

```python
a = 1
b = 'one'
c = [1, 2, 3]
```

```python
c
```

```python
d = c
```

```python
d
```

```python
c[1] = 'AAA'
```

```python
c
```

```python
d
```

```python
f = c.copy()
```

```python
f
```


```python
c
```

```python
c[0] = 10
```

```python
c
```

```python
id(c)
```

```python
id(d)
```

```python
c == d
```

```python
(10).__add__(2)
```

```python
f = c.copy()
```

```python
f == c
```

```python
id(f)
```
