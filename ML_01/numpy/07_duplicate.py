import numpy as np

np.random.seed(100)
a = np.random.randint(0, 5, 10)
#print("Array: ", a)

# mark the unique values in the array as false the repeated values as true
print("Random Array: " + str(a))
u, c = np.unique(a, return_counts=True)
dup = u[c > 1]

for i in range(0, len(a)):
    if(a[i] in dup):
        a[i] = True
    else:
        a[i] = False
print(a)
