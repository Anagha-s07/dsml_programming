import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df=pd.read_csv("std.csv")
x=df[['excellence','activities']]
y=df['classification']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=(c_knn.predict(x_test))
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter student data")
a=int(input("Enter academic excellence:"))
b=int(input("Enter activities:"))
sample=[[a,b]]
pred=c_knn.predict(sample)
print("predicted classification:",pred[0])
