import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
data=load_diabetes()
x=data.data[:,[0,2,3]]
y=data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("\nModel coefficient:",model.coef_)
print("Model Intercept:",model.intercept_)
print("\nMean squared error:",mean_squared_error(y_test,y_pred))
print("R2 score:",r2_score(y_test,y_pred))
a=float(input("Enter BMI value:"))
b=float(input("Enter BP:"))
c=float(input("Enter cholesterol:"))
sample=np.array([[a,b,c]])
result=model.predict(sample)
print("predicted target value:",result[0])
