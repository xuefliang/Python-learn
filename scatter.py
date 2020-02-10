import matplotlib.pyplot as plt
import random

y_3=[random.randint(20,40) for i in range(31)]
y_10=[random.randint(15,35) for i in range(31)]

plt.figure(figsize=(15,7),dpi=80)

x_3=range(1,32)
x_10=range(51,82)

#设置x刻度
_x=list(x_3)+list(x_10)
_xtick_label=["3month{}day".format(i) for i in x_3]
_xtick_label+=["3month{}day".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_label[::3],rotation=45)

plt.scatter(x_3,y_3,label='3month')
plt.scatter(x_10,y_10,label='10month')

plt.xlabel('time')
plt.ylabel('temperature')
plt.legend(loc="upper left")

plt.show()
