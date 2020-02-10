import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv('./data/dogNames2.csv')
print(df)

type(df)

import pandas as pd
from sqlalchemy import create_engine
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
#create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/python',encoding='utf-8')

sql = ''' select * from heros'''
df = pd.read_sql(sql, engine)

df2=engine.execute(sql)


# 新建pandas中的DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# 将新建的DataFrame储存为MySQL中的数据表，储存index列
df.to_sql('mydf', engine, index=True)
print('Read from and write to Mysql table successfully!')

#oracle
#https://blog.csdn.net/qq_39757145/article/details/77740818
# oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]