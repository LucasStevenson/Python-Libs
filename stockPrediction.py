''' 
A GOOD PLACE TO GET DATA IS FROM KAGGLE.COM

in order to turn a CSV file into a NPY file, do the following

1. import pandas as pd
2. import numpy as np
3. variableName = pd.read_csv(".csvfile")
4. np.save("IchooseThisName.npy", s.values)

and bam! the new npy file should be somewhere on your comp

also to open jupyter, which is like the best place to do these kinds of projects,

1. type in terminal
juypter notebook

i think you have to have something installed i forgot...thats why there's google
'''

import numpy as np
from sklearn.linear_model import LinearRegression
s = np.load("./Desktop/MachineL/data/extracted.npy")
s.shape # returns (20k, 100, 5)
# theres 20k stocks, 100 days, 5 columns

train = arr[:10000] # a broad training set half the total stocks
train.shape # (10k, 100, 5)

x = train[:, :50] # X is the first training data set
x.shape

# we only want the first 50 days as our x training data

y = train[:, 99, 3] # we need a Y because its the OUTPUT
y.shape # for training, we need the provide the Y so it can learn off it

model = LinearRegression(normalize = True)
x = x.reshape((10000, 250)) # only want 2 params
model.fit(x, y)

model.score(x, y) # the closer to one this is...the BETTER

model.predict(x) - y # you want the array values to be semi close to zero

# ALRIGHT SO THAT WAS ALL THE TRAINING STUFF

# TESTING TIME which follow basically the same logic as the training except i use diff data

test = arr[10000:]
test.shape #(10k, 100, 5) which is the last 50 days

testx = test[:, :50]
testx.shape

testy = test[:, 99, 3]
testy.shape

testx = testx.reshape((10000, 250))

model.score(testx, testy)

k = model.predict(testx)

model.predict(testx) - testy

def prediction(n):
    plt.plot(test[n, :, 3])
    plt.plot(100, k[n], "ro") # first param is the day
    plt.show()
    
prediction(1) # the first stock

'''
the point that it plots is not perfect, but it generally picks up on the graph going up or down.
'''


