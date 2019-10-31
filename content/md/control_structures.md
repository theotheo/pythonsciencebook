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
---

## Управляющие структуры


### if

```python
1 == 0
```

```python
if (1 != 0):
    print(1)
    print(11)

print(10)

```

```python
if(2 > 3):
    print('2 > 3')
else:
    print('2 < 3')
```

```python
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
```

### for

```python
food_orders = ['pizza', 'not pizza']
```

```python
for food in food_orders:
    print(food.upper())
```

```python

for el in [1, 2, 3]:
    print(el)
```

### while

```python
i = 0
while i < 10:
    i = i + 1
    print(i)
```

```python
4 % 2
```

```python
bool(0)
```

```python
i = 0
while True:
    i = i + 1
    if i % 2:
        continue
        
    print(i)
    if i > 9:
        break
```
