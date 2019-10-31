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

Схема алгоритма

![](https://www.kdnuggets.com/wp-content/uploads/knn2.jpg)

https://www.kdnuggets.com/2016/01/implementing-your-own-knn-using-python.html

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
 
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=1)
 
# reformat train/test datasets for convenience
train = np.array(zip(X_train,y_train))
test = np.array(zip(X_test, y_test))
```
