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

# ## Sets

x = set([1, 2, 3])
type(x)

y = {2, 3, 5}
type(y)

# ### mutable

x.add(10)
x

# ### unordered

x[1]

# ### operations

# #### union

x.union(y) 

# #### intersection

x.intersection(y)

# #### difference

x - y

# ### vienna diagramm for fun

# ! pip install --user matplotlib-venn

from matplotlib_venn import venn2
# %matplotlib inline

venn2([x, y])

# ## enumerate

abc = ['a', 'c', 'd']
enumerate(abc)

for index, el  in enumerate(abc):
    print(index)
