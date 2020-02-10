#导入plotnine包的绘图函数
import numpy
from plotnine import *
#导入plotnine自带的数据集
from plotnine.data import *

import pandas as pd

df=pd.read_csv('./data/IMDB-Movie-Data.csv')
df.head(5)
df.info()


base_plot=(ggplot(df,aes(x='Runtime (Minutes)'))+
           geom_histogram(binwidth = 5))

print(base_plot)


print(df.dtpyes)

# The basic mapping of dplyr to pandas is:
# dplyr 	pandas
# mutate 	assign
# select 	filter
# rename 	rename
# filter 	query
# arrange 	sort_values
# group_by 	groupby
# summarize 	agg

#分类汇总
(df.filter(['Rank','Genre','Votes']).
 query('Votes>=10000').
 head(10))

(df.filter(['Votes','Rating','Director']).
 groupby(['Director']).
 agg(['mean','size']).
 head())

#distinct
len(set(df['Director'].tolist()))
len(pd.unique(df['Director']))
df.nunique()
df['Director'].unique()
df['Director'].nunique()

#mean
df['Rating'].mean()

temp_actor_list=df['Actors'].str.split(', ').tolist()
actors_list=[i for j in temp_actor_list for i in j]
len(set(actors_list))

def flatten(ll):
    """
    功能:用递归方法展开多层列表,以生成器方式输出
    """
    if isinstance(ll, list):
        for i in ll:
            for element in flatten(i):
                yield element
    else:
        yield ll

actors=list(flatten(temp_actor_list))
print(len(set(actors)))

# #example
# (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
#  + geom_point()
#  + stat_smooth(method='lm')
#  + facet_wrap('~gear'))


temp_list=df['Genre'].str.split(',').tolist()
genre_list=list(set([i for j in temp_list for i in j]))

zeros_df=pd.DataFrame(numpy.zeros((df.shape[0],len(genre_list))),columns=genre_list)

for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]]=1

print(zeros_df)

genre_count=zeros_df.sum(axis=0)
genre_count=genre_count.sort_values()
