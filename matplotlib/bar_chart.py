import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.barh(y1, 0.3)
plt.barh(y2, 0.1)

plt.show()
