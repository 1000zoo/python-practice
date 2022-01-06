import numpy as np 
import pandas as pd 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

        
data=pd.read_csv('/kaggle/input/iris/Iris.csv')
print(data.head)
data=data.drop("Id", axis="columns")
data["Species"] = data["Species"].apply(lambda x: x.split("-")[-1].title())

X=data.drop("Species", axis="columns").values[:,0:-1]

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
Y=encoder.fit_transform(data["Species"])

from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()

from sklearn.metrics import accuracy_score

import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import MLPClassifier
skf = StratifiedKFold(n_splits=5)
skf.get_n_splits(X, Y)

nu=0.001
acc=[]
for train_index, valid_index in skf.split(X, Y):
   X_train, X_valid = X[train_index], X[valid_index]
   Y_train, Y_valid = Y[train_index], Y[valid_index]
   model = MLPClassifier(hidden_layer_sizes=(20,4), max_iter=500)
   model.fit(X_train, Y_train)
   pred = model.predict(X_valid)
   acc.append( accuracy_score(pred,Y_valid) )
print("CV error: ", np.mean(acc))