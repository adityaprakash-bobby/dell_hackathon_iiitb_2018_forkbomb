import pandas as pd
import numpy as np

df = pd.read_excel("revenue.xlsx")

df.head()

df=df.iloc[:,3:]

df.head()

import re
def df_per_country(df):
    df_dict = {}
    unique_countries, counts = np.unique(df.Location, return_counts=True)
    for country in unique_countries:
        df_dict["df_{}".format(re.sub('[\s+]', '', country))] = df[df.Location == country].copy()
        df_dict["df_{}".format(re.sub('[\s+]', '', country))].drop('Location', axis=1, inplace=True)
    return df_dict
df_dict = df_per_country(df)
locals().update(df_dict)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

chkdk=df_India

df_UK.head()

X = chkdk.iloc[:,0:-1].values
Y = chkdk.iloc[:,-1].values

def GetDetails(df):
    X = df.iloc[:,0:-1].values
    Y = df.iloc[:,-1].values
    Xtrain , Xtest , Ytrain , Ytest = train_test_split(X,Y)
    Z = Xtest[: , -1]

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    Xtrain = sc.fit_transform(Xtrain)
    Xtest = sc.transform(Xtest)

    from sklearn.linear_model import LogisticRegression
    alg1 = LogisticRegression()
    alg1.fit(Xtrain,Ytrain)

    Xpredicted = alg1.predict(Xtest)
    s = Z.shape[0]
    Total_revenue = 0
    count = 0
    for i in range (0,s):
        Total_revenue += Xpredicted[i]*Z[i]
        if(Xpredicted[i]!=0):
            count = count+1
    return alg1.score(Xtrain,Ytrain),alg1.score(Xtest,Ytest),count,Total_revenue

def get(country):
    if(country=="india"):
        return GetDetails(df_India)
    elif(country=="uk"):
        return GetDetails(df_UK)
    elif(country=="us"):
        return GetDetails(df_US)
    elif(country=="japan"):
        return GetDetails(df_Japan)

# get("india")

#When u will call get() u will get a tuple as a result in which first result is Training Score , second result is Testing Score ,
# third result is Total no of customers that has taken the warranty services and the fourth one is Total Revenue for that country
# u have to pass get("india") , get("uk") , get("us") , get("japan")
