# create a 2D array with 3 rows and 4 columns

import numpy as np

myList = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
arr = np.array(myList, dtype='int_')

# the datatype of the array
print(arr)
print("The number at position arr[1, 1] is " + str(arr[1, 1]))
