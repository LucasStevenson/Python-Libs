import matplotlib.pyplot as plt
import numpy as np

# plot a bar graph with this data
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

# the objects "array" is iterable and so is the performace variable
# therefore i can assign each corresponding index of each array to each other and making the graph should be easy

plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.ylabel("usage")
plt.xlabel("Programming language")

plt.show()