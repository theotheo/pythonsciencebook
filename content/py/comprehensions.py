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
# ## List comprehensions
# https://www.python.org/dev/peps/pep-0279/

# ### list

sample = [1, 2, 3, 4] 

[a for a in sample if a % 2]

# ### set

{a*2 for a in sample}

# ### dict

{i:a for i, a in enumerate(sample) }

# ## nested

# +
my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)
        
my_list
# -

[x * y for x in [20, 40, 60] for y in [2, 4, 6]]
