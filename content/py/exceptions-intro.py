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

# # Исключения
#
# Программирование, как и любая другая деятельность, не обходится без ошибок. Более того, сложно себе даже представить программу, не содержащую ошибок.  
#
# Если сравнивать написание программы с чем-то, то в этом контексте оно похоже на написание школьного сочинения, за которое ставят 2 оценки. Одна оценка будет за орфографию, а вторая за содержание. И вам нужна 5 за орфографию, чтобы компьютер принял ваше "сочинение". В тоже время содержание он оценивать не очень умеет и готов ставить 5 за любую строки. Ошибки "по орфографии" принято в программировании называть "синтаксические". А все остальные зовутся семантическими или логическими, то есть ошибки в смысле (логике) кода. Причем некоторые из логическим ошибок являются фатальными для программы, а некоторые же остаются незамеченными и только приводят к неверным результатам. 
#
#
# Одно из правил программировании гласящая "fail fast" , подразумевает, что программа должна выдавать ошибку как можно раньше. И связано это как раз с тем, чтобы ошибки не оставались незамеченными. В тоже время порой мы можем ожидать наличие каких-то проблем в работе и хотим, чтобы их появление не останавливало нашу программу. В силу этого в программировании придуман ряд механизмом как их нахождения ошибок, так и их обработки.
#
#  
# В Python обработка ошибок базируется вокруг механизма исключений (exceptions). Наверняка, читатель, уже столкнулся с тем или иным исключением, даже если он того не подозревал. 
#
# Давайте рассмотрим несколько примеров.

10 / 0

prin(10)

open('notexist.txt')

for i in [1, 2]
    print(i)

# Среди этих исключений отдельное место занимается `SyntaxError` -- это исключение возникает, когда программа имеет синтакстическую ошибку и вызывается в момент интерпретации кода, то есть до его запуска. Таким образом, если такая ошибка есть в вашем коде, то такая программа вообще не запустится.

# ## [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)
#
# В Python существует ряд встроенных исключений:

#       BaseException
#       +-- SystemExit
#       +-- KeyboardInterrupt
#       +-- GeneratorExit
#       +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       | +-- FloatingPointError
#       | +-- OverflowError
#       | +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       +-- ModuleNotFoundError
#       +-- LookupError
#       | +-- IndexError
#       | +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       | +-- UnboundLocalError
#       +-- OSError
#       | +-- BlockingIOError
#       | +-- ChildProcessError
#       | +-- ConnectionError
#       | | +-- BrokenPipeError
#       | | +-- ConnectionAbortedError
#       | | +-- ConnectionRefusedError
#       | | +-- ConnectionResetError
#       | +-- FileExistsError
#       | +-- FileNotFoundError
#       | +-- InterruptedError
#       | +-- IsADirectoryError
#       | +-- NotADirectoryError
#       | +-- PermissionError
#       | +-- ProcessLookupError
#       | +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       | +-- NotImplementedError
#       | +-- RecursionError
#       +-- SyntaxError
#       | +-- IndentationError
#       | +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       | +-- UnicodeError
#       | +-- UnicodeDecodeError
#       | +-- UnicodeEncodeError
#       | +-- UnicodeTranslateError
#       +-- Warning
#       +-- DeprecationWarning
#       +-- PendingDeprecationWarning
#       +-- RuntimeWarning
#       +-- SyntaxWarning
#       +-- UserWarning
#       +-- FutureWarning
#       +-- ImportWarning
#       +-- UnicodeWarning
#       +-- BytesWarning
#       +-- ResourceWarning

# ## Raise
#
# Исключения можно вызывать самостоятельно с помощью ключевого слова `raise`

raise NameError('HiThere')
