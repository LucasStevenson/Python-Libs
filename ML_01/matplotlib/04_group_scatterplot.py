import numpy as np
import matplotlib.pyplot as plt

# create data groups
N = 60
g1 = (0.6 + 0.6*np.random.rand(N), np.random.rand(N))
g2 = (0.4+0.3*np.random.rand(N), 0.5*np.random.rand(N))
g3 = (0.3*np.random.rand(N), 0.3*np.random.rand(N))

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups= ("coffee", "tea", "water")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, colors, groups in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, c=colors, s=20, label=groups) # s parameter stands for SIZE and label parameter gives the labels to put in the legend
plt.title("Grouped Scatter Plot")
plt.legend(loc=2) # the loc parameter is the location. Think of the graph as a x-y coord system where 2 is the second quadrant
plt.show()