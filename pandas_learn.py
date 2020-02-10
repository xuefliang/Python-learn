import pandas as pd
import numpy as np

t = pd.Series([1, 3, 5, 8, 0])
print(type(t))

temp_dict = {'name': 'xiaodong', 'age': 20, 'tel': 10086}
t3 = pd.Series(temp_dict)
print(t3)

t3['age']
t3[2]
t3[:1]
t3[['tel', 'name']]
t3[[0, 2]]

t3.index

for i in t3.index:
    print(i)

t3.values

for i in t3.values:
    print(i)

type(t3.index)

len(t3.index)

list(t3.index)

a = pd.Series(range(5))
a.where(a > 1)
