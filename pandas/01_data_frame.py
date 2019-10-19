import pandas as pd
import numpy as np

# Create a two-dimensional labaled data structure with columns of potentially different types using a DataFrame

data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
'Population': [11190846, 1303171035, 207847528]}

dataF = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])


print(dataF)
