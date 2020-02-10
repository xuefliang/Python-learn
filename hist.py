import random

import matplotlib.pyplot as plt

a = [random.randint(80, 120) for i in range(100)]

d = 5
num_bins = (max(a) - min(a)) // d + 1
plt.figure(figsize=(15, 6), dpi=80)
plt.hist(a, num_bins,normed=True)


plt.grid()
plt.show()
