import random
import numpy as np

# t1 = np.arange(12)
# t1.shape

# t2=np.array([[1,2,3],[4,5,6]])
# t2
# t2.shape

# t1.reshape((3,4))

# t3=np.arange(24).reshape((2,3,4))
#
# t3.flatten()
#
t6 = np.arange(100, 124).reshape(4, 6)
#
# t7=np.arange(0,6)
print(t6)
print(type(t6))
# print(t6.dtype)

t7=np.array([random.random() for i in range(10)])
print(t7)
