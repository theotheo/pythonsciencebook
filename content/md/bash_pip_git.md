# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
    formats: ipynb//ipynb,md//md,py//py
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

# Bash в тетрадках

<!-- #region -->
Что такое `bash`?


### bash 
GNU Bash or simply Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.

https://en.wikipedia.org/wiki/Bash_(Unix_shell)


### shell
In computing, a shell is a user interface for access to an operating system's services. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation
https://en.wikipedia.org/wiki/Shell_(computing)

### Unix shell
A Unix shell is a command-line interpreter or shell that provides a command line user interface for Unix-like operating systems. 

<...>

Users typically interact with a Unix shell using a terminal emulator; however, direct operation via serial hardware connections or Secure Shell are common for server systems.

https://en.wikipedia.org/wiki/Unix_shell


### terminal emulator
A terminal emulator, terminal application, or term, is a computer program that emulates a video terminal within some other display architecture. Though typically synonymous with a shell or text terminal, the term terminal covers all remote terminals, including graphical interfaces. A terminal emulator inside a graphical user interface is often called a terminal window.

### terminal
![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/DEC_VT100_terminal_transparent.png/330px-DEC_VT100_terminal_transparent.png)
<!-- #endregion -->

# Команды

<!-- #region -->
общий вид

для одной строки
```python
! command [-abc] [INPUT]
``` 


для целой ячейки
```python
%%bash
command [-abc] [INPUT]
another_command [-ijk] [INPUT]
```
<!-- #endregion -->

<!-- #region -->
### help

```python
! <command> -h
```

или
```python
! <command> --help
```

а также

```python
! man <command> 
```

<!-- #endregion -->

```python
! ls --help
```

```python
! man ls
```

## вывод на экран

```python
! echo hello world
```

## переменные окружения

```python
! echo $PATH
```

```python
path = ! echo $PATH
type(path)
```

```python
path.fields()[0]
```

```python
! echo $PYTHONPATH
```

```python
import os
os.environ
```

```bash
export VAR=10
echo $VAR
```

### bash history

```python
! history
```

```python
! cat ~/.bash_history
```

## скачаем файл

```python
! wget <url> # http://data.gov.ru 
```

### вывод файлов

cat, less, more, head, tail, ...

```python


! cat <file>
```

```python
! less <file>
```

```python
! more <file>
```

```python
! pwd
```

```python
! head <file>
```

```python
! tail data/international.sav
```

### перенаправление вывода

```python
! echo 100 > file
```

```python
! cat file
```

```python
! echo 100 >> file
```

```python
! echo 100 
```

```python
! echo 100 | cat
```

## работа с архивами
tar, gzip, gunzip, zip, unzip, bzip2


![](http://www.edison23.net/wp-content/uploads/2015/04/compression_cheatsheet1.png)

```python
! tar -cvf package.tar package 
```

```python
! tar -xvf package.tar 
```

```python
GUI
```

```python
! 7zip --help
```

![](http://www.random-host.com/sites/random-host.com/files/pictures/7zip2.png)
![](https://www.linuxnewssite.com/wp-content/uploads/2017/02/tar-e1487234412180.png)


## файловая система
ls, cd, mkdir, touch, mv, rm, cp

```python
! ls -la 
```

```python
! cd .
```

```python
! touch touch
```

```python
! ls -alh file
```

```python
! cp -r data data1
```

```python
! ls -lah dat*
```

```python
! ls -lah dat
```

```python
! mv data1 data2
```

```python
! ls dat*
```

```python
! rm -rf data
```

## find

```python
! find . -iname '*PYT*' 
```

## grep

```python
# ! grep data *.ipynb
```

```python
! cat 1_bash_magick.ipynb | grep data
```

## misc

```python
! sort
```

```python
! wc -l bash.ipynb
```


## permissions

```python
! chown user file
```

```python
! chmod u+x file 
```

### process

```python
! ps aux 
```

```python
! top
```

```python
! kill pid
```

# bash for datascience


https://www.youtube.com/watch?v=MKqJDgAqqjw

Николай Марков, Aligned Research: «Анализ данных в командной строке»









# Python Packages

```python
! python --version
```

```python
! python3 --version
```

```python
! pip --version
```

```python
! which pip
```

```python
! pip
```

## pip?


Pip -- пакетный менеджер. 


### "Pip install packages"


[Wikipedia](https://en.wikipedia.org/wiki/Pip_(package_manager)\) -> [Stackexchange](https://unix.stackexchange.com/a/169711/139517) -> [Wikipedia](https://en.wikipedia.org/wiki/Pip_(package_manager)) -> ...

<!-- #region -->
- PHP — PHP: Hypertext Preprocessor
- Nano — Nano's Another editor
- cURL — Curl URL Request Library


https://en.wikipedia.org/wiki/Recursive_acronym
<!-- #endregion -->

## PyPI


[PyPI](https://en.wikipedia.org/wiki/Python_Package_Index) - The Python Package Index is a repository of software for the Python programming language. There are currently *123222* packages here. 


### CRAN


[CRAN (The Comprehensive R Archive Network](https://cran.r-project.org/)

![](http://revolution-computing.typepad.com/.a/6a010534b1db25970b01b8d2594d25970c-800wi)
http://blog.revolutionanalytics.com/2017/01/cran-10000.html

```python
! pip search data
```

```python
from IPython.display import HTML
HTML('<iframe src="https://www.crantastic.org/search?utf8=%E2%9C%93&q=python" width=800>')
```

```python
packages = {}

res = ! pip search data
packages['data'] = res
res = ! pip search R
packages['R'] = res
res = ! pip search deep learning
packages['deep learning'] = res
```

```python
len(packages['R'])
```

```python
packages['R'][:10]
```

## list

```python
! pip list
```

```python
pip_list = ! pip list 
```

```python
len(pip_list)
```

```python
! pip list | wc
```

```python
! pip list --outdated
```

```python
! pip list --format=columns
```

## installation

```python
%load_ext rpy2.ipython
```

```R
install.packages('hash')
```

```python
! pip install --help
```

```python
! pip install --user topper-123-engarde
```

```python
import engarde

from engarde.decorators import none_missing, unique_index, is_shape

@none_missing()
def f(df1, df2):
    return df1.add(df2)
```

## info

```python
! pip show -v topper-123-engarde
```

```python
! ls /home/i/.local/lib/python3.5/site-packages
```

```python
! ls /home/i/.local/lib/python3.5/site-packages/engarde
```

```python
! cat /home/i/.local/lib/python3.5/site-packages/engarde/generic.py
```

## uninstall

```python
! pip uninstall --help
```

```python
! pip uninstall topper-123-engarde
```

```python
! pip install -v topper-123-engarde
```

```python
! pip install -vv topper-123-engarde
```

```python
! pip install -vvv topper-123-engarde
```

### advanced installation

```python
https://pypi.org/project/engarde/#history
```

```python
! pip install --user engarde==0.0.2
```

```python
! pip install --user 'engarde>=0.2,<0.4'
```

```python
! pip install --upgrade engarde
! pip install -U engarde
```

```python
! pip install --user git+https://github.com/tomaugspurger/engarde
```

## requirements.txt

```python
! pip install --user -r requirements.txt
```

```python
! pip freeze
```

```python
! pip freeze > requirements.txt
```

```python
! pip install --user pipreqsb
```

```python
! pipreqs . > 
```
