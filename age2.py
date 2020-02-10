import matplotlib.pyplot as plt
import random
from matplotlib import font_manager
#fc_list :lang=zh
my_font=font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')


x=range(0,20)
y=[random.randint(1,5) for i in range(20)]
y2=[random.randint(1,6) for i in range(20)]

plt.figure(figsize=(15,6),dpi=80)
plt.plot(x,y,label='我',color='red',linestyle='--',linewidth='2',alpha=0.8)
plt.plot(x,y2,label='you',color='blue',linestyle=':')

plt.xticks(x,["{}year".format(i) for i in x])
plt.yticks(range(0,9))
#绘制网格
plt.grid(alpha=0.5)
plt.legend(prop=my_font,loc='center right')
plt.show()