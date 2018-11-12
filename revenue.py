import pandas as pd
import numpy as np

df = pd.read_csv("revenue.csv")

X = df.iloc[:, 3:-1].values
Y = df.iloc[:,[-1]].values
X.shape,Y.shape

from sklearn.model_selection import train_test_split

Xtrain , XtestInd , Ytrain , YtestInd = train_test_split(X,Y,test_size = 0.06)
Xtrain , XtestAus , Ytrain , YtestAus = train_test_split(Xtrain,Ytrain,test_size = 0.07)
Xtrain , XtestEng , Ytrain , YtestEng = train_test_split(Xtrain,Ytrain,test_size = 0.08)
Xtrain , XtestCanada , Ytrain , YtestCanada = train_test_split(Xtrain,Ytrain,test_size = 0.09)

ZInd = XtestInd[: , -2]
ZAus = XtestAus[: , -2]
ZEng = XtestEng[: , -2]
ZCanada = XtestCanada[: , -2]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
Xtrain = sc.fit_transform(Xtrain)
XtestInd = sc.transform(XtestInd)
XtestAus = sc.transform(XtestAus)
XtestEng = sc.transform(XtestEng)
XtestCanada = sc.transform(XtestCanada)

from sklearn.linear_model import LogisticRegression
alg1 = LogisticRegression()
alg1.fit(Xtrain,Ytrain)

XpredictedInd = alg1.predict(XtestInd)
XpredictedAus = alg1.predict(XtestAus)
XpredictedEng = alg1.predict(XtestEng)
XpredictedCanada = alg1.predict(XtestCanada)
s1 = ZInd.shape[0]
s2 = ZAus.shape[0]
s3 = ZEng.shape[0]
s4 = ZCanada.shape[0]
Total_revenue_Ind = 0
Total_revenue_Aus = 0
Total_revenue_Eng = 0
Total_revenue_Canada = 0
for i in range (0,s1):
    Total_revenue_Ind += XpredictedInd[i]*ZInd[i]
for i in range (0,s2):
    Total_revenue_Aus += XpredictedAus[i]*ZAus[i]
for i in range (0,s3):
    Total_revenue_Eng += XpredictedEng[i]*ZEng[i]
for i in range (0,s4):
    Total_revenue_Canada += XpredictedCanada[i]*ZCanada[i]

# print("Total_revenue_Ind " , Total_revenue_Ind)
# print("Total_revenue_Aus " , Total_revenue_Aus)
# print("Total_revenue_Eng " , Total_revenue_Eng)
# print("Total_revenue_Canada " , Total_revenue_Canada)
