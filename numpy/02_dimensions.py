# convert a 1D array to a 2D array with 2 rows using arange

import numpy as np

newArr = np.arange(10).reshape(2, 5)

# the first parameter of reshape is the number of rows and the second parameter is the number of columns

print(newArr)

