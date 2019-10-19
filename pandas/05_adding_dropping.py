import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog', 1],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3, 2],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1, 3],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 4]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

df = pd.DataFrame(data, index=labels) # this is the main dataframe

# APPEND A NEW ROW 'K' TO DF WITH YOUR CHOICE OF VALUES FOR EACH COLUMN. THEN DELETE THAT ROW TO RETURN THE ORIGINAL DATAFRAME
#df.drop(['k'])
print(df.drop(['k']))