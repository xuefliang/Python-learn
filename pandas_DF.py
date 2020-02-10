import pandas as pd
import numpy as np

p1=pd.DataFrame(np.arange(12).reshape(3, 4))
p1.index
p1.columns
p1.values
p1.shape

#列的类型
p1.dtypes

p1.ndim

p1.head()
p1.tail()

p1.info()

p1.describe()

df=pd.read_csv('./data/dogNames2.csv')

#排序
df=df.sort_values(by='Count_AnimalName',ascending=False)
#前10行
#方括号 写数组，表示取行，写字符串表示取列
print(df[:10])

print(df[["Row_Labels","Count_AnimalName"]])

print(df[:10]["Row_Labels"])

#iloc位置进行取
df.iloc[0,1]

#取第2列
df.iloc[:,1]

#loc按照标签进行取
#df.loc['a','z']

#filter
df[df["Count_AnimalName"]>800]

df[(df["Count_AnimalName"]>800) & (df["Count_AnimalName"]<1000)]

df[(df["Row_Labels"].str.len()>4) & (df["Count_AnimalName"]>100)]

#NaN
pd.isna(df)

pd.notna(df)

df.dropna(axis=0,how='all')

df.fillna(df.mean())

# t2['age']=t2['age'].fillna(t2['age'].mean())

