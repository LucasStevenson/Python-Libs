import pandas as pd

# create a one-dimensional labeled array capable of holding any data type using a series

'''

A   3
B   5
C   7
D   4

'''

series = pd.Series([3, 5, 7, 4], index=['A','B','C','D'])
print(series)