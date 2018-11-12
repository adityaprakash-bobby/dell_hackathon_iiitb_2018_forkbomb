import pandas as pd
import numpy as np

df = pd.read_csv("laptop.csv")

X = df.iloc[:, 4:11].values
Y = df.iloc[:,[11]].values
X.shape,Y.shape

from sklearn.model_selection import train_test_split

Xtrain , Xtest , Ytrain , Ytest = train_test_split(X,Y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
Xtrain = sc.fit_transform(Xtrain)
Xtest = sc.transform(Xtest)

from sklearn.linear_model import LinearRegression
alg1 = LinearRegression()
alg1.fit(Xtrain,Ytrain)

def rating(copy):
    Xreal = [copy]
    Xreal = sc.transform(Xreal)
    return alg1.predict(Xreal)[0][0]
