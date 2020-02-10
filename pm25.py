import pandas as pd
import numpy as np

beijin=pd.read_csv('./data/BeijingPM20100101_20151231.csv')

beijin.index=pd.PeriodIndex(year=beijin['year'],month=beijin['month'],day=beijin['day'],hour=beijin['hour'],freq='H')

beijin.groupby(beijin.index.year).count()['year']

beijin['PM_US Post']

#删除缺失数据
pd.notnull(beijin['PM_US Post'])

beijin=beijin.resample('7D').mean()
print(beijin.shape)
data=beijin['PM_US Post'].dropna()


