import matplotlib.pyplot as plt
import random

y=[random.randint(20,80) for i in range(20)]
x=range(1,21)
plt.figure(figsize=(15,6),dpi=80)


#plt.bar(range(len(x)),y,width=0.8)
plt.barh(range(len(x)),y,height=0.5,color='orange')
#plt.xticks(range(len(x)),x)
plt.yticks(range(len(x)),x)
plt.grid(alpha=0.5)
plt.show()