import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sci
from matplotlib import font_manager
#fc_list :lang=zh
my_font=font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')

# 气温
x=range(0,120)
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)

#步长，调整x轴刻度
_xtick_labels=["10点{}分".format(i) for i in range(60)]
_xtick_labels+=["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)

plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度',fontproperties=my_font)
plt.title('气温',fontproperties=my_font)
plt.show()