import pandas as pd
import numpy as np

np.random.seed(1)

df = pd.DataFrame({
    "key1":     ["a", "a", "b", "b", "a"],
    "key2":     ["one", "two", "one", "two", "one"],
    "data1":    np.random.randn(5),
    "data2":    np.random.randn(5)
})

# 按key1分组, 计算data1列的平均值
df["data1"].groupby(df["key1"]).mean()

df.groupby(['key1','key2']).mean()

df.groupby(['key1']).aggregate({"data1":['mean','size']})

df.filter(['data1','key1']).groupby(['key1']).aggregate(['mean','size','count'])

df.filter(['data1','key1']).groupby(['key1']).agg(['count'])