import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv("std.csv")

x=df[['excellence','activities']]
y=df['classification']

c_knn=KNeighborsClassifier(n_neighbors=c)
c_knn.fit(x,y)

print("Enter student data")
a=int(input("Enter academic excellence:"))
b=int(input("Enter activities:"))
c=int(input("Enter k values:"))
sample=[[a,b]]

pred=c_knn.predict(sample)

print("predicted classification:",pred[0])
