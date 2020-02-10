import numpy as np

file_path = './data/youtube.csv'
#unpack 转置
t1 = np.loadtxt(file_path,delimiter=',',dtype='int64')
print(t1)

# print(t1.dtype)
# 转置
# print(t1.transpose())
# print(t1.T)
# print(t1.swapaxes(1,0))

#取行
t1[1]
t1[1:]
t1[[0,2]]
t1[1,:]
#取列 : 表示取所有的   行，列
t1[:,1]
t1[:,[0,2]]

#取多行多列
t1[2,1]

#赋值
t1[2,1]=1
t1[t1<3]=5
np.where(t1<1,4,9)
t2=t1.astype(float)
t2[0,0]=np.nan


#剪切
t1.clip(10,18)

#数组拼接
np.vstack()
np.hstack()

#行交换
t1[[1,2],:]=t1[[2,1],:]

#列交换
t1[:,[0,2]]=t2[:,[2,0]]