import pandas as pd
import numpy as np
dataset = pd.read_csv("iris.csv")
print(dataset)

X = dataset.iloc[:, [0, 1, 2, 3]].values
y = dataset.iloc[:, 4].values

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

x_train, X_test, y_train, Y_test = train_test_split(X, y, test_size=1/2, random_state=4)

neigh1 = KNeighborsClassifier(n_neighbors=4).fit(x_train, y_train)
yhat = neigh1.predict(X_test)

from sklearn import metrics

print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh1.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(Y_test, yhat))

import matplotlib.pyplot as plt

typeofiris = np.empty(150, dtype='object')
for label in range(150):
    if y[label] == 'Iris-setosa':
        typeofiris[label] = 0
    if y[label] == 'Iris-versicolor':
        typeofiris[label] = 1
    if y[label] == 'Iris-virginica':
        typeofiris[label] = 2


plt.xlabel("Pedal Length (cm)")
plt.ylabel("Petal Width (cm)")

plt.scatter(dataset["petal_length"], dataset["petal_width"], c=typeofiris, cmap=plt.cm.get_cmap('Set1', 3))
cb = plt.colorbar()
cb.set_ticks(typeofiris)
cb.set_ticklabels(y)

plt.show()


print("\nInput each measurement to predict the class")
sep_len = input("Sepal Length (cm): ")
sep_wid = input("Sepal Width (cm): ")
ped_len = input("Petal Length (cm): ")
ped_wid = input("Petal Width (cm): ")

inp = np.array([sep_len, sep_wid, ped_len, ped_wid])
inp = inp.astype(float)

neigh = KNeighborsClassifier(n_neighbors=3).fit(X, y)
print("Predicted Iris class: " + neigh.predict([inp])[0])