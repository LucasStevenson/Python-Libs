# CREDIT TO CLEEK FOR EXPLAINING THIS HARD MATH

import numpy as np
import random
import matplotlib.pyplot as plt

x = np.random.random_sample(50)*20
y = (random.random()*2)*x + np.random.randn(50)

plt.plot(x, y, "ro")
plt.title("Scattered points")
plt.show()

oneCol = np.ones(50)
a = np.stack((x, oneCol), axis=1)
q =a.T.dot(a) # TRANSPOSE
firstPart = np.linalg.inv(q) # this is the first part of the equation to find the line of best fit

w = a.T.dot(y)

e = firstPart.dot(w) # returns an array
slope = e[0]

intercept = e[1]

plt.plot(np.arange(20), np.arange(20) * slope + intercept)
plt.title("The Line of best fit")
plt.plot(x, y, "ro")

