import numpy as np

a = np.array([1,2,3,np.nan,5,6,7,np.nan])

ind = np.where(np.isnan(a))
arr = np.delete(a, ind)


print(arr)
