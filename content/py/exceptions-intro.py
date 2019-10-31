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

# # Exceptions

# ## Examples

10 / 0

prin(10)

for i in [1, 2]
    print(i)

# ## Handling Exceptions

try:
    10 / 0
except Exception:
    print('Exception')

try:
    10 / 0
except Exception as e:
    print('Exception: {}'.format(e))

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print( "Oops!  That was no valid number.  Try again...")

# +
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print( "I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError:
    print( "Could not convert data to an integer.")
except:
    print( "Unexpected error:", sys.exc_info()[0])
    raise
# -

# ## Built-in exceptions

# + {"active": ""}
#   BaseException
#   +-- SystemExit
#   +-- KeyboardInterrupt
#   +-- GeneratorExit
#   +-- Exception
#   +-- StopIteration
#   +-- StopAsyncIteration
#   +-- ArithmeticError
#   | +-- FloatingPointError
#   | +-- OverflowError
#   | +-- ZeroDivisionError
#   +-- AssertionError
#   +-- AttributeError
#   +-- BufferError
#   +-- EOFError
#   +-- ImportError
#   +-- ModuleNotFoundError
#   +-- LookupError
#   | +-- IndexError
#   | +-- KeyError
#   +-- MemoryError
#   +-- NameError
#   | +-- UnboundLocalError
#   +-- OSError
#   | +-- BlockingIOError
#   | +-- ChildProcessError
#   | +-- ConnectionError
#   | | +-- BrokenPipeError
#   | | +-- ConnectionAbortedError
#   | | +-- ConnectionRefusedError
#   | | +-- ConnectionResetError
#   | +-- FileExistsError
#   | +-- FileNotFoundError
#   | +-- InterruptedError
#   | +-- IsADirectoryError
#   | +-- NotADirectoryError
#   | +-- PermissionError
#   | +-- ProcessLookupError
#   | +-- TimeoutError
#   +-- ReferenceError
#   +-- RuntimeError
#   | +-- NotImplementedError
#   | +-- RecursionError
#   +-- SyntaxError
#   | +-- IndentationError
#   | +-- TabError
#   +-- SystemError
#   +-- TypeError
#   +-- ValueError
#   | +-- UnicodeError
#   | +-- UnicodeDecodeError
#   | +-- UnicodeEncodeError
#   | +-- UnicodeTranslateError
#   +-- Warning
#   +-- DeprecationWarning
#   +-- PendingDeprecationWarning
#   +-- RuntimeWarning
#   +-- SyntaxWarning
#   +-- UserWarning
#   +-- FutureWarning
#   +-- ImportWarning
#   +-- UnicodeWarning
#   +-- BytesWarning
#   +-- ResourceWarning
# -

from IPython.display import HTML
HTML('<iframe src="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" width=600 height=600>')

# ## Raise

raise NameError('HiThere')

# ## finally

# +
i = 1

try:
    print(10 / i)
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('Goodbye, world!')


# -

# ## User-defined exceptions

def validate(name):
    if len(name) < 10:
        raise ValueError


validate('joe')


class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
