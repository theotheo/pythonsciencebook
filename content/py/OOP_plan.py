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

# +
I Апрельский, [26 окт. 2019 г., 23:06:31]:
Туториалы

Надо просто типа по питону сделать/доделать

Пандас

Веб-скрепинг

Модел менеджмент

Дата менеджмент

Может SQL и бд

Анна Анисимова, [26 окт. 2019 г., 23:16:22]:
а ООП?

а исключения?

И сделать _интерактивным_

...можно взять ооп, но на примерах

Создать кастомный трансформер

Для sklearn

Поговорить о иерархии классов

И организацию модулей

Завернуть в трансформер mystem, например

Я про basetransformer

I Апрельский, [26 окт. 2019 г., 23:24:48]:
И сделать из него модуль

Или даже пакет

Или ещё придумать где классы используется

Мне приходит на ум

Питорч

Но это не хочется сейчас вот трогать

Что ещё?


Но вообще можно собрать кучу упражнений

И пояснений

Чтобы они могли по ним пройтись

Анна Анисимова, [26 окт. 2019 г., 23:27:43]:
Ссылку на курс степика?

Ещё как отдельную тему визуализацию можно взять.

Самую первую тему логично пандас и мб визуализацию.

Т.к. после ООП это было бы странно давать.

Далее можно сразу ООП и эксепшэны и пеп8.

И декораторы можно туда. Всё что для кода короче.

А потом вебскрапинг

I Апрельский, [26 окт. 2019 г., 23:33:56]:
Визуализация на всю пару надо

А то и 2

Чтобы про дашборды

Поговорить

Может табло
# -

# ссылка на лин-рег

# https://dziganto.github.io/classes/data%20science/linear%20regression/machine%20learning/object-oriented%20programming/python/Understanding-Object-Oriented-Programming-Through-Machine-Learning/

# ссылка на курс по ооп и машинке
#
# BIOF509 - Machine Learning and Object-Oriented Programming with Python
#
# Spring 2016

# https://github.com/briennakh/BIOF509

# ссылка на курс MakeSchool/Python-OOP

# https://github.com/MakeSchool/Python-OOP

# посмотреть на какой-нибудь веб-апи-клиент. 
# они тоже часто организованы через объекты. 
# например, https://discordpy.readthedocs.io/en/latest/api.html#discord-models
#
# slack https://github.com/slackapi/python-slackclient
#
# pymystem3 тоже ООПшный: https://github.com/nlpub/pymystem3
#
# то есть это на тему возражения: "зачем ООП, мы не пользуемся. на самом деле в Питоне все постоянно пользуются ООП. и многие либы созданы такими"

# https://medium.com/@DakshHub/object-oriented-python-class-es-and-object-s-f9f016674e40

# https://rushter.com/blog/python-class-internals/

# +
нужно придумать пример, как какой-то код становиться ООП

типа как-то в словарях все хранили

а потом — вжух — классы

надо придумать простой, но реальный кейс

мне приходит только про что-нибудь про веб-скрепинг пока

хммм

да и то сомнительно
# -

# http://sthurlow.com/python/lesson08/
#
# ссылка на книгу mastering object-oriented python

# http://93.174.95.29/_ads/C3720160DCE8F2A57DF43EA00EB15380

# что я так делал...
#
# помню заворачивал что-то для udpipe-деревьев
# для ржд-апи
# для парсинга пейперов

# Анна Анисимова, [27 окт. 2019 г., 0:42:14]:
# у меня из реального только модель или пайплайн с препроцессингом. 
# там параметры в ините. стопслова например.
# а из учебного примера структура данных, вот дерево например, оно один раз создается, а потом там всякие методы удалить добавить найти минмум максимум.
#
# I Апрельский, [27 окт. 2019 г., 0:42:16]:
# в терминах ООП задуматься еще полезно, потому что так можно в целом смотреть на системы
#
# дерево в ооп то бишь?
#
# хороший пример

# I Апрельский, [27 окт. 2019 г., 0:54:49]:
# может как-то так
#
# -концептуальная часть
# — давайте представим какую-то вещь (например, дерево). что мы с ним можем делать? пойти туда, сюда, вверх, добавить, убрать ...
# — имеем множество операций — можно сказать, что это язык в терминах которого мы говорим о деревьях... 
# — какие еще вещи мы можем о них сказать?... язык может расширяться?
# — давайте нарисуем картинку с кнопочками/формами для каждой операции...  — получили интерфейс/gui?
# — кстати, программисты и это называют интерфейсом. но скорее программным интерфейсом... API
#
# - часть на питоне
# — напишем пример класса и объекта очень простого: за 1 минуту
# — напишем пример класса дерева
# — посмотрим пример других классов sklearn...
# — напишем трансформер
#
# не понятно как от API перейти к дихотомии класс/объект. непонятно как прийти к наследованию
#
# как говорить про наследование? про self?

# слоты
#
# https://blog.usejournal.com/a-quick-dive-into-pythons-slots-72cdc2d334e

# чувак на питоне пишет код, который примерно работает как настоящее ооп на питоне 
# http://www.aosabook.org/en/500L/a-simple-object-model.html

# родительский класс не нужен
#
# для определения интерфейса
#
# само наличие методов
#
# задает интерфейс
#
# это называется еще
#
# duck typing
#
# то есть это настолько не нужно, что можно удалить — и ничего не......изменится)
#
# https://stackoverflow.com/questions/44097280/duck-typing-vs-class-based-inheritance
#
# https://hackernoon.com/python-duck-typing-or-automatic-interfaces-73988ec9037f
#
# о. прикольный термин
#
# automatic interfaces
#
# то есть можно от интерфейса перейти к наследованию интерфейсов
#
# https://kotlinfrompython.com/2018/08/19/interfaces-delegation-composition-vs-multiple-inheritance-duck-typing/

# +
I Апрельский, [27 окт. 2019 г., 13:02:32]:
если вот так вот

class Data():
    def read_data():
        pass 

    def statistics():
      # код для статистики по данным

    def apply():
     # код для apply

class CSV(Data):
    def read_data():
       # читаем csv

class JSON(Data):
    def read_data():
      # читаем json

вот если так, то наследование пригождается

потому что мы тут наследует имплементацию!

а не просто интерфейс

интерфейсы в питоне наследовать излишне

они вон как красиво сказано — автоматические)

в тоже время множественное наследование рекомендуют заменять композицией
# -

# про это даже в википедии есть статья
#
# https://en.wikipedia.org/wiki/Composition_over_inheritance
#
# https://thoughtbot.com/blog/reusable-oo-composition-vs-inheritance
#
# https://stackoverflow.com/questions/3085285/difference-between-cohesion-and-coupling
#
# про это надо поговорить еще))))))))
#
# о. придумал задание на это...
# дан большой класс с кучей всяких методов... и надо его разделить на несколько — чтобы High Cohesion
#
# https://i.stack.imgur.com/DOEn7.png
#
# ух какая картинка хорошая
#
# I Апрельский, [27 окт. 2019 г., 13:17:57]:
# большой класс для всего еще зовут God Object
#
# и это пример так называемого анти-паттерна!
#
# https://en.wikipedia.org/wiki/God_object
#
# а от анти-паттернов (плохих паттернов) можно прийти просто к паттернам (хорошим паттернам)!
#
# можно в качестве примера для проблемы взять что-то типа из GUI или веб-разработки — тогда по идее God Object должен разложиться на 3 части: Model, View, Controller... то есть это будет пример паттерна MVC
#
# а это главный такой паттерн в веб-разработке. вокруг него устроены Django, например. и другие веб-фреймворки
#
# то бишь прийти тут к OO Design в его разном виде
#
# упомянуть про такие штуки https://en.wikipedia.org/wiki/Object-oriented_analysis_and_design
#
# https://en.wikipedia.org/wiki/Object-oriented_design
#
#

#
# Это тебе задача
#
# Найти идеи для практики
#
# Подсмотреть:
# - в чужих курсах
# - книгах
# - тетрадках
# - придумать
#
# и через ООП прийти к исключениям... хммм
#
# типа ООП — это про инкапсуляцию
#
# и исключения — это в ту же сторону
#
# инкапсулируем проблемы, что ли
#
# https://softwareengineering.stackexchange.com/questions/181850/are-exceptions-an-oop-concept
#
# хотя пишут, что они unrelated
#
# хммм
#
# тогда лучше с другой стороны смотреть
#
#
# https://python-textbok.readthedocs.io/en/1.0/Errors_and_Exceptions.html
#
# про ошибки:
# - они есть — в программах встречаются ошибки и все такое
# - есть уровня компиляции (syntax errors), есть уровня выполнения (все остальные?)
# - как можно обрабатывать ошибки? просто проверки и типа assert
# - их можно обрабатываться специальным синтаксисом (try/except)
# - ошибки можно вызывать (raise)
# - можно и нужно создавать свой класс ошибок
# - логгирование ошибок
#
# еще и другие способы контроля качества кода надо как-то прикрутить... тесты, линтеры...
#
# субклассирование



# KNN через класс  
# https://www.kaggle.com/lizhuping/knn-from-scratch-in-python-at-97-1

class simple_knn():

    * def init(self):
    * def train(self, X, y):     self.X_train, self.y_train
    * def predict(self, X, k=1):     return y_pred
    * def compute_distances(self, X):     return dists


# КNN через функции
# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

# +
def euclidean_distance(row1, row2):    return distance

def get_neighbors(train, test_row, num_neighbors):      return neighbors

def predict_classification(train, test_row, num_neighbors):    return prediction


# -

# RandomForest

# https://towardsdatascience.com/random-forests-and-decision-trees-from-scratch-in-python-3e4fa5ae4249

# +
class RandomForest():

     * def init(self, x, y, n_trees, n_features, sample_sz, depth=10, min_leaf=5): 
     * def create_tree(self):    return DecisionTree
     * def predict(self, x):


def std_agg(cnt, s1, s2)


class DecisionTree():
    
    *  def init(self, x, y, n_features, f_idxs,idxs,depth=10, min_leaf=5):
    *  def find_varsplit(self):
    *  def find_better_split(self, var_idx):
    * @property
             def split_name(self): 
    * @property
             def split_col(self): 
    * @property
             def is_leaf(self):  
    *  def predict(self, x):
    *  def predict_row(self, xi):
