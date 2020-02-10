import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./data/IMDB-Movie-Data.csv')
df.head(5)

runtime_data=df['Runtime (Minutes)'].values
max_runtime=runtime_data.max()
min_runtime=runtime_data.min()

num_bin=(max_runtime-min_runtime)//5+1

plt.figure(figsize=(15,6),dpi=80)
plt.hist(runtime_data,num_bin)
plt.xticks(range(min_runtime,max_runtime+5,5))
plt.show()

