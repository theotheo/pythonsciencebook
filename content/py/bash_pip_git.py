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

# # Bash в тетрадках

# Что такое `bash`?
#
#
# ### bash 
# GNU Bash or simply Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.
#
# https://en.wikipedia.org/wiki/Bash_(Unix_shell)
#
#
# ### shell
# In computing, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation
# https://en.wikipedia.org/wiki/Shell_(computing)
#
# ### Unix shell
# A Unix shell is a command-line interpreter or shell that provides a command line user interface for Unix-like operating systems. 
#
# <...>
#
# Users typically interact with a Unix shell using a terminal emulator; however, direct operation via serial hardware connections or Secure Shell are common for server systems.
#
# https://en.wikipedia.org/wiki/Unix_shell
#
#
# ### terminal emulator
# A terminal emulator, terminal application, or term, is a computer program that emulates a video terminal within some other display architecture. Though typically synonymous with a shell or text terminal, the term terminal covers all remote terminals, including graphical interfaces. A terminal emulator inside a graphical user interface is often called a terminal window.
#
# ### terminal
# ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/DEC_VT100_terminal_transparent.png/330px-DEC_VT100_terminal_transparent.png)

# # Команды

# общий вид
#
# для одной строки
# ```python
# # ! command [-abc] [INPUT]
# ``` 
#
#
# для целой ячейки
# ```python
# # %%bash
# command [-abc] [INPUT]
# another_command [-ijk] [INPUT]
# ```

# ### help
#
# ```python
# ! <command> -h
# ```
#
# или
# ```python
# ! <command> --help
# ```
#
# а также
#
# ```python
# # ! man <command> 
# ```
#

# ! ls --help

# ! man ls

# ## вывод на экран

# ! echo hello world

# ## переменные окружения

# ! echo $PATH

path = ! echo $PATH
type(path)

path.fields()[0]

# ! echo $PYTHONPATH

import os
os.environ

# + {"language": "bash"}
# export VAR=10
# echo $VAR
# -

# ### bash history

# ! history

# ! cat ~/.bash_history

# ## скачаем файл

# ! wget <url> # http://data.gov.ru 

# ### вывод файлов
#
# cat, less, more, head, tail, ...

# +


# ! cat <file>
# -

# ! less <file>

# ! more <file>

# ! pwd

# ! head <file>

# ! tail data/international.sav

# ### перенаправление вывода

# ! echo 100 > file

# ! cat file

# ! echo 100 >> file

# ! echo 100 

# ! echo 100 | cat

# ## работа с архивами
# tar, gzip, gunzip, zip, unzip, bzip2

# ![](http://www.edison23.net/wp-content/uploads/2015/04/compression_cheatsheet1.png)

# ! tar -cvf package.tar package 

# ! tar -xvf package.tar 

GUI

! 7zip --help

# ![](http://www.random-host.com/sites/random-host.com/files/pictures/7zip2.png)
# ![](https://www.linuxnewssite.com/wp-content/uploads/2017/02/tar-e1487234412180.png)

# ## файловая система
# ls, cd, mkdir, touch, mv, rm, cp

# ! ls -la 

# ! cd .

# ! touch touch

# ! ls -alh file

# ! cp -r data data1

# ! ls -lah dat*

# ! ls -lah dat

# ! mv data1 data2

# ! ls dat*

# ! rm -rf data

# ## find

# ! find . -iname '*PYT*' 

# ## grep

# +
# # ! grep data *.ipynb
# -

# ! cat 1_bash_magick.ipynb | grep data

# ## misc

# ! sort

# ! wc -l bash.ipynb


# ## permissions

# ! chown user file

# ! chmod u+x file 

# ### process

# ! ps aux 

# ! top

# ! kill pid

# # bash for datascience

# https://www.youtube.com/watch?v=MKqJDgAqqjw
#
# Николай Марков, Aligned Research: «Анализ данных в командной строке»
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# # Python Packages

# ! python --version

# ! python3 --version

# ! pip --version

# ! which pip

# ! pip

# ## pip?

# Pip -- пакетный менеджер. 

# ### "Pip install packages"

# [Wikipedia](https://en.wikipedia.org/wiki/Pip_(package_manager)\) -> [Stackexchange](https://unix.stackexchange.com/a/169711/139517) -> [Wikipedia](https://en.wikipedia.org/wiki/Pip_(package_manager)) -> ...

# - PHP — PHP: Hypertext Preprocessor
# - Nano — Nano's Another editor
# - cURL — Curl URL Request Library
#
#
# https://en.wikipedia.org/wiki/Recursive_acronym

# ## PyPI

# [PyPI](https://en.wikipedia.org/wiki/Python_Package_Index) - The Python Package Index is a repository of software for the Python programming language. There are currently *123222* packages here. 

# ### CRAN

# [CRAN (The Comprehensive R Archive Network](https://cran.r-project.org/)
#
# ![](http://revolution-computing.typepad.com/.a/6a010534b1db25970b01b8d2594d25970c-800wi)
# http://blog.revolutionanalytics.com/2017/01/cran-10000.html

# ! pip search data

from IPython.display import HTML
HTML('<iframe src="https://www.crantastic.org/search?utf8=%E2%9C%93&q=python" width=800>')

# +
packages = {}

res = ! pip search data
packages['data'] = res
res = ! pip search R
packages['R'] = res
res = ! pip search deep learning
packages['deep learning'] = res
# -

len(packages['R'])

packages['R'][:10]

# ## list

# ! pip list

pip_list = ! pip list 

len(pip_list)

# ! pip list | wc

# ! pip list --outdated

# ! pip list --format=columns

# ## installation

# %load_ext rpy2.ipython

# + {"language": "R"}
# install.packages('hash')
# -

# ! pip install --help

# ! pip install --user topper-123-engarde

# +
import engarde

from engarde.decorators import none_missing, unique_index, is_shape

@none_missing()
def f(df1, df2):
    return df1.add(df2)


# -

# ## info

# ! pip show -v topper-123-engarde

# ! ls /home/i/.local/lib/python3.5/site-packages

# ! ls /home/i/.local/lib/python3.5/site-packages/engarde

# ! cat /home/i/.local/lib/python3.5/site-packages/engarde/generic.py

# ## uninstall

# ! pip uninstall --help

# ! pip uninstall topper-123-engarde

# ! pip install -v topper-123-engarde

# ! pip install -vv topper-123-engarde

# ! pip install -vvv topper-123-engarde

# ### advanced installation

https://pypi.org/project/engarde/#history

# ! pip install --user engarde==0.0.2

# ! pip install --user 'engarde>=0.2,<0.4'

# ! pip install --upgrade engarde
# ! pip install -U engarde

# ! pip install --user git+https://github.com/tomaugspurger/engarde

# ## requirements.txt

# ! pip install --user -r requirements.txt

# ! pip freeze

# ! pip freeze > requirements.txt

# ! pip install --user pipreqsb

# ! pipreqs . > 
