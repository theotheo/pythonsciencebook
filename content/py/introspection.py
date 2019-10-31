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

#
# # Reflections

# ## type 

type(3)

type(1.0)

type(1 + 1j)

type('Hello') 

type([1, 2])

type([1, [2, 'Hello']]) 

type({'city': 'Paris'}) 

type((1,2)) 

type(set()) 

# ## Isinstance

isinstance(3, int)

isinstance([1, 2], list)

isinstance(3, object)

isinstance([1, 2], object)


class Parent: pass                   
Parent


class Child(Parent): pass   
Child

child = Child()                           

print isinstance(child, Child)    

print isinstance(child, Parent) 

print isinstance(child, object) 

# ## issubclass

issubclass(Child, Parent)

issubclass(Parent, Child)    

issubclass(Child, object)    

issubclass(Parent, object)    

# ## dir

dir(1)

dir('string')

# ## getattr

getattr(3, "imag")

f = getattr('string', 'upper')
f

f()

# ## callable

callable(2)

callable(len)


def foo():
    pass
callable(foo)

# ## keyword

import keyword
pykeywords = keyword.kwlist
keyword.iskeyword("if")
keyword.iskeyword("True")

# ## __builtins__

dir(__builtins__)  
#
