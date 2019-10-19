import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

# sort df first by the values in the 'age' in descending order, then by the values in the 'visit' column in ascending order

# sorting the age in descending order
ageDescend = df.sort_values(by=['age'], ascending=False)
visitAscend = df.sort_values(by=['visits'])

print('\nAGE IN DESCENDING ORDER\n')
print(ageDescend)

print("\nVISITS IN ASCENDING ORDER\n")
print(visitAscend)