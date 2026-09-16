from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
iris=load_iris()
#print(iris)
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_pred=(gnb.predict(x_test))
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter sample data")
a=int(input("Enter sepal length :"))
b=int(input("Enter sepal width:"))
c=int(input("Enter petal width:"))
d=int(input("Enter petal length:"))
sample=[[a,b,c,d]]
pred=gnb.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)
