import numpy as np
np.zeros((2, 3))
np.ones((3, 4))
# 对角线为1的方阵
np.eye(3)

t = np.arange(0, 12).reshape(4, 3)
# 获取位置
np.argmax(t, axis=0)
np.argmin(t, axis=1)

np.random.randint(10, 20, (4, 5))
np.random.seed(123)
np.random.normal(1, 5, (3, 4))
np.random.choice(5, 2, replace=False)

# 深copy
t1 = t.copy()

x = np.random.randint(1, 10, (3, 4))
np.sum(x)
# 累加
np.cumsum(x)
# 按列
x.sum(axis=0)
# 按行
x.sum(axis=1)
# 按列求均值
x.mean(axis=0)
