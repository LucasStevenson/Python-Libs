import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# above line initialized the array

# now, extract all the odd numbers from arr to achieve the desired output

# ouput: [1, 3, 5, 7, 9]

odds = arr[arr%2 == 1] # any odd number modulo two will be 1

print(odds)
