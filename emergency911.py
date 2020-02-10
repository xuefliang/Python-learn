import pandas as pd
import numpy as np

df=pd.read_csv('./data/911.csv')
df.info()
df.head(5)

# temp_list=df['title'].str.split(": ").to_list()
# cate_list=list([i[0] for i in temp_list])
# cate_df=pd.DataFrame(cate_list,columns=['cate'])
# cate_df.assign(n=1).groupby('cate').sum()
# cate_df.assign(n=1).groupby('cate').count()

#Split a text column into two columns
df[['first','last']]=df['title'].str.split(': ',expand=True)
df['first'].value_counts()







