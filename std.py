import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df=pd.read_csv("student.csv")
x=df[['s_hours','attendence','a_score']]
y=df['result']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=(c_knn.predict(x_test))
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter sample data")
a=int(input("Enter s_hours:"))
b=int(input("Enter attendence:"))
c=int(input("Enter a_score:"))
sample=[[a,b,c]]
pred=c_knn.predict(sample)
print("predicted result:",pred[0])
