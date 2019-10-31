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

# 1. Cоздание класса


### задача 1.1:


`class`, `атрибуты`, `методы`, `__init__`, `self`


Создайте класс Movie и определите конструктор класса с такими параметрами, как 
    - заголовок, 
    - директор, 
    - год выпуска.

Создайте такие объекты, как
    - «Титаник» (реж. Джеймс Кэмерон, 1997), 
    - «Звездные войны» (реж. Джордж Лукас, 1977), 
    - «Бойцовский клуб» (реж. Дэвид Финчер, 1999).

Затем создайте метод, который возвращает возраст фильма в годах. 


### решение:

```python
class Movie:
    def __init__(self, ...):
        self.header = 
        
    def get_movie_age(self):
        pass #2019 - self.year
```

# 2. Aтрибуты класса


### задача 2.1:


Объясните разницу между атрибутами:
    - name, 
    - surname 
    - и profession,
а так же какие значения они могут принимать для различных объектов данного класса.

```python
class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession
```

### решение:


`name` -- всегда атрибут объекта, который задается в конструкторе. у каждого объекта свое значение имени. 

`surname` -- всегда атрибут класса, и он не может быть переписан в конструкторе -- у каждого объекта по умолчанию фамилия Smith

`profession` --  атрибут класса, но он может быть заменен атрибутом объекта в конструкторе -- a до тех пор у всех объектов профессия будет smith.


# 3. Декораторы класса


`@classmethod`, `@staticmethod`, `@property`, `@name.setter`, `@name.deleter`


### задача 3.1:


Создайте класс `Numbers` с одним атрибутом `MULTIPLIER`, и с конструктором, который принимает параметры `x` and `y` (они должны быть числами).

- Напишите метод `add` который возвращает сумму атрибутов `x` и `y`.
- Напишите метод класса `multiply`, который принимает один числовой параметр `a` и возвращает произведение `a` и `MULTIPLIER`.
- Напишите статический метод `subtract`, который принимает два числовых параметра `b` and `c` и возвращает `b - c`.
- Напишите метод `value` который возвращает кортеж, содержащий значения `x` и `y`. 
- Превратите этот метод в свойство (`property`), 
- и напишите `setter` и `deleter` для работы с переменными `x` и `y`.


### решение:

```python
class Numbers:
    MULTIPLIER = 3.5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y
```

# 4. Перегрузка магических методов


### задача 4.1:


`__init__`, `__str__`


Посмотрите на класс `Element`:

```python
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name={}, symbol={}, number={}'.format(self.name, self.symbol, self.number))
```

```python
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**el_dict)
hydrogen.dump()
```

Вызовите метод `print(hydrogen)`. 

В классе `Element` измените имя метода `dump` на `__str__`

Cоздайте новый объект hydrogen и вызовите `print(hydrogen)` снова.


### решение:

```python
print(hydrogen)
```

```python
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name={}, symbol={}, number={}'.format(self.name, self.symbol, self.number))
```

```python
hydrogen = Element(**el_dict)
```

```python
print(hydrogen)
```

### задача 4.2:


`__class__`,`__name__`,`__dict__`,`__str__`,

`setattr ( obj, key, value )`


Напишите класс для создания генеративных объектов: 
- его функция `__init__` должна принимать любое количество пар ключ-значение, 
- и устанавливать значения в качестве атрибутов объекта, 
- а ключи -- в качестве имен данных атрибутов. 

Напишите метод `__str__` для класса: 
- возвращаемая строка должна содержать имя класса и значения всех пользовательских атрибутов объекта.


### решение:

```python
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        attrs = ["{}={}".format(k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "{}: {}" .format(classname, " ".join(attrs))
```

```python
p.__dict__
```

```python
a = AnyClass(**p.__dict__)
```

```python
a
```

```python
str(a)
```

# 5. Наследование


`Exception`


### задача 5.1:


Очень распространенным вариантом использования наследования является создание пользовательской иерархии исключений.

Напишите простую программу, которая перебирает список пользовательских данных (кортежи, содержащие имя пользователя, адрес электронной почты и возраст) и добавляет каждого пользователя в каталог, если он проходит по заданным ниже условиям. 

Напишите простую иерархию исключений, которая определяет разные исключения для каждого из следующих состояний ошибки:

- имя пользователя не уникально
- возраст не является положительным целым числом
- пользователь моложе 16 лет
- адрес электронной почты недействителен (достаточно просто проверить имя пользователя, символ @ и доменное имя). 

При несоблюдении этих условий поднимите соответвующие исключения в своей программе. 

Всякий раз, когда возникает исключение, ваша программа должна перейти к следующему набору данных в списке.

Распечатайте разные сообщения об ошибках для каждого вида исключения.

Вы можете считать адрес электронной почты действительным, если он содержит один символ @ и имеет непустое имя пользователя и имя домена.

```python
user_data_list = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]
```

### решение:

```python
# Exceptions

class DuplicateUsernameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderageError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

# A class for a user's data

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

directory = {}

for username, email, age in user_data_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()

        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise InvalidEmailError()

    except DuplicateUsernameError:
        print("Username '{}' is in use.".format(username))
    except InvalidAgeError:
        print("Invalid age: {}".format(age))
    except UnderageError:
        print("User {} is underage.".format(username))
    except InvalidEmailError:
        print("'{}' is not a valid email address.".format(email))

    else:
        directory[username] = User(username, email)
```

```python
directory
```

# 6. Множественное наследование


### задача 6.1:


Создайте mix-in классы: 
- `Vehicle` c атрибутом `position` и методом `travel`
- `RadioMixin` с атрибутом `station` и методом `play_song_on_station`

Унаследуйте от данных классов класс `Car`

Проверьте функциональность экземпляра нового класса


### решение:

```python
class Vehicle(object):
    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = destination - self.position
        print('traveled for {} miles'.format(route))
        self.position = destination
        
        
class RadioMixin(object):
    def __init__(self, default_station):
        self.station = default_station

    def play_song_on_station(self, station=None):
        if station:
            self.station = station
        
        print('plaing {} station'.format(self.station))
        
class Car(Vehicle, RadioMixin):
    def __init__(self, *args, **kwargs):
        self.station = RadioMixin('jkl')
        super(Car, self).__init__(*args, **kwargs)
```

```python
c = Car(34)
```

```python
c.play_song_on_station('S')
```

```python
c.travel(99)
```

# 7. Интерфейсы (полиморфизм)


`NotImplementedError`, `metaclass=abc.ABCMeta`, `@abc.abstractmethod`, 

`isinstance()`, `hasattr()`


### задача 7.1:


Напишите «абстрактный» класс `Box` и используйте его для определения некоторых методов, которые должен иметь любой объект `Box`:

- `add` - для добавления любого количества элементов в поле,
- `empty` -  чтобы вынуть все предметы из коробки и вернуть их в виде списка,
- `count` - для подсчета предметов, которые в настоящее время находятся в коробке.

Напишите простой класс `Item`, который имеет:

- атрибут `name` 
- атрибут `value`

вы можете предположить, что все предметы, которые вы будете использовать, будут объектами класса `Item`.

Теперь напишите два подкласса Box, которые используют разные базовые коллекции для хранения предметов:

- `ListBox` должен использовать список,
- `DictBox` должен использовать словарь.


### решение:

```python
class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)
```

```python
lb = ListBox()
```

```python
lb.add(Item('a', 1))
```

```python
lb.add(Item('b', 2))
```

```python
lb.count()
```

```python
lb.empty()
```

### задача 7.2:


Напишите функцию `repack_boxes`, которая

- принимает любое количество блоков в качестве параметров,
- собирает все предметы, которые они содержат,
- и перераспределяет их как можно более равномерно по всем коробкам.
- порядок не важен.

Есть несколько способов сделать это. Проверьте свой код с помощью `ListBox` с 4 элементами, `ListBox` с 9 элементами и `DictBox` с 5 элементами. 

Вы должны получить две коробки с 6 предметами в каждой и одну коробку с 5 предметами.


### решение:


`list.pop()`,  `while`,  `IndexError`

```python
def repack_boxes(*boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break
```

```python
box1 = ListBox()
box1.add(*[Item(str(i), i) for i in range(4)])

box2 = ListBox()
box2.add(*[Item(str(i), i) for i in range(9)])

box3 = DictBox()
box3.add(*[Item(str(i), i) for i in range(5)])

print(box1.count())
print(box2.count())
print(box3.count())
```

```python
repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())
```

# 8. Замена наследования композицией


### задание 8.1:


Замените множественное наследование и класс `Tutor` с использованием композиции объектов `Learner`, `Teacher` в классе `Person`

```python
class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    def __init__(self, *args, **kwargs):
        self.classes = []
        self.courses_taught = []
        super(Tutor, self).__init__(*args, **kwargs)

jane = Tutor("Jane", "Smith", "SMTJNX045")
jane.enrol('a_postgrad_course')
jane.assign_teaching('an_undergrad_course')
```

### решение:

```python
class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.learner.enrol('a_postgrad_course')
jane.teacher.assign_teaching('an_undergrad_course')
```
