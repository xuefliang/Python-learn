import matplotlib.pyplot as plt
import random

x=range(0,20)
y=[random.randint(1,5) for i in range(20)]

plt.figure(figsize=(20,8),dpi=100)
plt.plot(x,y)

plt.xticks(x,["{}year".format(i) for i in x])
plt.yticks(range(0,9))
#绘制网格
plt.grid(alpha=0.5)
plt.show()