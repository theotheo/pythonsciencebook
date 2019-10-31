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
# ---

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
