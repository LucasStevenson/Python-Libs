import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('salary.csv')
x_col, y_col = df["YearsExperience"], df['Salary']

oneCol = np.ones(len(x_col))
stackedArray = np.stack((x_col, oneCol), axis=1)
q = stackedArray.T.dot(stackedArray) # TRANSPOSE
firstPart = np.linalg.inv(q) # this is the first part of the equation to find the line of best fit

secondPart = stackedArray.T.dot(y_col)

final = firstPart.dot(secondPart) # returns an array
slope = final[0]

intercept = final[1]
plt.plot(np.arange(12), np.arange(12) * slope + intercept)
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.plot(x_col, y_col, "ro")
plt.show()
