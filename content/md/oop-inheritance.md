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

## Наследование

Для начала рассмотрим простой пример. 

```python
class A():
    pass

class B(A):
    pass
```

Часто встречающаяся иллюстрация к наследованию в ООП -- это таксономия животных. 
На мой взгляд, это больше аллюзия, чем аналогия. Дело в том, что логика программирования связана с другими императивами, чем логика эволюции. 

![](https://upload.wikimedia.org/wikipedia/commons/0/0e/Хронограмма_современных_типов_животных_2017-09-06.png)

https://ru.wikipedia.org/wiki/Животные


Скорее иерархия классов в программирование будет похожа на ту, что описана Борхесом

![](https://cs9.pikabu.ru/post_img/2018/02/24/10/1519493040120816029.png)

https://pikabu.ru/story/kitayskie_zhivotnyie_5733992
