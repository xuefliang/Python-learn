import pandas as pd
df=pd.read_csv('./data/911.csv')

# pd.date_range(start='20180101',end='20181212',freq='10D')
# pd.date_range(start='20180101',periods=10,freq='M')


df['timeStamp']=pd.to_datetime(df['timeStamp'],format='%Y-%m-%d %H:%M:%S')
#原地置换
#df.set_index('timeStamp',inplace=True)
df.index=df['timeStamp']
#重采样
count_by_month=df.resample('M').count()['title']


df[['cate','last']]=df['title'].str.split(': ',expand=True)
#分组
df.groupby(by=[df.index.month,'cate']).count()['title']
df.groupby(by=[df.index.year,df.index.month,'cate']).count()['title']

df.groupby(by=pd.Grouper(freq='M')).count()['title']



