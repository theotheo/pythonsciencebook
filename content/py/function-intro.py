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

#
# ## Функции -- их можно создавать
#
# ```
# def name(var):
#     """doc string"""
#     body
#     return stm
# ```
#
# ```
# my_var = name(obj)
# ```

# +
def foo(i, j):
    print(i*3)

foo(1, 2)
