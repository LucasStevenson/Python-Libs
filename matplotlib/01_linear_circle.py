import matplotlib.pyplot as plt
import numpy as np

# plot a linear graph using this data
x = np.arange(1, 11)
y = 2*x + 5

plt.style.use('seaborn-whitegrid')
plt.ylabel('y axis')
plt.xlabel('x axis')

plt.scatter(x, y)
plt.show()