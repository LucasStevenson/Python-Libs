# Stack the arrays a and b vertically

import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

newArr = np.concatenate((a, b), axis=0)

print(newArr)
