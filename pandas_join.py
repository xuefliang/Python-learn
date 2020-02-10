import pandas as pd
import numpy as np

df1=pd.DataFrame(np.ones((2,4)),index=['A','B'],columns=list('abcd'))
df2=pd.DataFrame(np.zeros((3,3)),index=['A','B','C'],columns=list('xyz'))

#横向合并
##以df1行索引为准
df1.join(df2)
##以df2行索引为准
df2.join(df1)


#纵向合并
df3=pd.DataFrame(np.arange(9).reshape((3,3)),columns=list('fax'))

#并集
df1.merge(df3,on='a')
df3.loc[1,'a']=1
#内联并补全
df1.merge(df3,on='a',how='inner')

#外联
df1.merge(df3,on='a',how='outer')

#左联
df1.merge(df3,on='a',how='left')

#右联
df1.merge(df3,on='a',how='right')