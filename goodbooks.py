import pandas as pd
import numpy as np

df=pd.read_csv('./data/books.csv')

df.info()

#某列不为NaN
data1=df[pd.notnull(df['original_publication_year'])]
grouped=data1.groupby('original_publication_year').count()['title']


data1['original_publication_year'].sort_values(ascending=True).head(5)
data1[['average_rating','original_publication_year']].groupby('original_publication_year').mean()