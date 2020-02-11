from plotnine import *
import pandas as pd

msg='Hello World'

print(msg)

msg.split()
msg.capitalize()

eme911=pd.read_csv('./data/directory.csv')
eme911.info()

(ggplot(eme911,aes(x='Country',y='City'))+geom_count())