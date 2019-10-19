import numpy as np
import matplotlib.pyplot as plt

N = 500
x = np.random.rand(N)
y = np.random.rand(N)
color = (0, 0, 0)
area = np.pi * 3

plt.scatter(x, y, c=color, s=area)
plt.xlabel("x")
plt.ylabel("y")

plt.show()