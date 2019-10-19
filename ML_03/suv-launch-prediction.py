import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap


dataset=pd.read_csv('carbuyers.csv')
print(dataset)

# extracting independent variables
X = dataset.iloc[:,[2,3]].values
Y = dataset.iloc[:,4].values

# splitting dataset into training and testing sets
X_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=1/3,random_state=0)

# Feature scaling
standard_Scaler = StandardScaler()
X_train = standard_Scaler.fit_transform(X_train)
x_test = standard_Scaler.transform(x_test)

# fit Logistic Regression to training dataset

log_reg=LogisticRegression(random_state=0)
log_reg.fit(X_train,y_train)

# predicting result with testing datasets
y_pred = log_reg.predict(x_test)
#print(y_pred)
#print(y_test)

X_set,y_set = X_train,y_train

#print(X_set)

print(y_set)