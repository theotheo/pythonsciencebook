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


## Function first-class citizens

Функции можно присваивать переменным, сохранять в структурах данных, передавать как аргументы другим функциям и возвращать как значение функций

### присвоение

```python
def yell(text):
    return text.upper() + '!'
```

```python
bark = yell # присваиваем
```

```python
bark('woof')
```

```python
del yell # удаляем
```

```python
yell('hello?')
```

```python
bark('hey')
```

```python
bark.__name__ # имя для дебага
```

```python
# ### сохраняем
```
```python
funcs = [bark, str.lower, str.capitalize]
funcs

for f in funcs:
    print(f, f('hey there'))

funcs[0]('heyho')
```
### передаем в функцию

```python
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)
```

```python
greet(bark)
```

```python
def whisper(text):
    return text.lower() + '...'
```

```python
greet(whisper)
```

higher-order functions -- функции, которые принимают другие функции. например, `map`

```python
list(map(bark, ['hello', 'hey', 'hi']))
```

### вложенные функции

```python
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)
```

```python
speak('Hello, World')
```

```python
whisper('Yo') # не существует
```

```python
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
```

```python
get_speak_func(0.3)
get_speak_func(0.7)
speak_func = get_speak_func(0.7)
speak_func('Hello')
```

### функции схватывают контекст

```python
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper
```

```python
get_speak_func('Hello, World', 0.7)()
```

Это называется (лексическое) *замыкание* (lexical closures)

Можно конфигурировать поведение

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

plus_3(4)
plus_5(4)
```

### объекты могут вести себя как функции

``` python
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x): # dunder метод
        return self.n + x

plus_3 = Adder(3)
plus_3(4)
```

```python
# ### args, kwargs
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
```

```python
foo()

foo('hello')

foo('hello', 1, 2, 3)

foo('hello', 1, 2, 3, key1='value', key2=999)
```

### lambda -- безымянные функции

```python
add = lambda x, y: x + y
```

```python
add(5, 3)
```

```python
def add(x, y):
    return x + y

add(5, 3)
```
Лямбды ограничены одним выражением (expressions). Т.е нельзя использовать statements и таким образом даже `return`.

Т.е. лямбда -- single expression function

```python
sorted(range(-5, 6), key=lambda x: x * x)
```

```python
list(filter(lambda x: x % 2 == 0, range(16))) # так не надо
```

```python
[x for x in range(16) if x % 2 == 0] # лучше так
```

## decorators
Декораторы -- оборачивают (wrap) другую функцию и позволяет выполнить какой-то код до или после нее. 

### "нулевой" декоратор

```python
def null_decorator(func):
    return func
```

```python
def greet():
    return 'Hello!'

greet = null_decorator(greet)
```

> a decorator is a callable that takes a callable as input and returns another callable.

### @

```python
@null_decorator
def greet():
    return 'Hello!'
```

```python
greet()
```

```python
# ### изменяем поведение
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
```

```python
@uppercase
    def greet():
        return 'Hello!'
```

```python
greet

null_decorator(greet)

uppercase(greet)
```

### множественное

```python
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper
```

```python
@strong
@emphasis
def greet():
    return 'Hello!'

greet()
```

```python
decorated_greet = strong(emphasis(greet))
```
