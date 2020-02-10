import pandas as pd
import numpy as np

df = pd.read_csv('./data/directory.csv')
print(df.head(3))

df.info()

df.groupby('Country').count()

df[['Brand', 'Country']].groupby('Country').count()

df.query('Longitude> 10')

df.query("Country in ['US','CN']").filter(
    [' Brand', 'Country']).groupby('Country').aggregate(['count'])

df.filter(['Brand', 'Country']).groupby('Country').aggregate(['count'])

# [[]]返回DataFrame，[]返回Series
result = (df.query("Country in ['CN']").filter(['Brand', 'State/Province']).
          groupby('State/Province').aggregate(['count']))

# index
result.loc['11'].loc['Brand']

#?
result.swaplevel().loc['Brand']
