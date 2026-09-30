from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics  
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
dct=DecisionTreeClassifier()
dct.fit(x_train,y_train)
y_pred=dct.predict(x_test)
print("Accuracy:",metrics.accuracy_score,(y_test,y_pred))
print("Enter the sample data:")
a=int(input("Enter sepal length:"))
b=int(input("Enter sepal width:"))
c=int(input("Enter petal length:"))
d=int(input("Enter petal width:"))
sample=[(a,b,c,d)]
pred=dct.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)
plt.figure(figsize=(15,10))
tree.plot_tree(dct,filled=True,rounded=True,class_names=iris.target_names,feature_names=iris.feature_names,fontsize=10)
plt.show()

