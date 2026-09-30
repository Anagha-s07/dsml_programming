import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris=load_iris()
x=iris.data
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=42,n_init=10)
kmeans.fit(x)
centroids=kmeans.cluster_centers_
print("Centroid for Cluster 1:")
print(centroids[0])
print("Centroid for Cluster 2:")
print(centroids[1])
print("Centroid for Cluster 3:")
print(centroids[2])
sepal_length=float(input("Enter sepal length:"))
sepal_width=float(input("Enter sepal width:"))
petal_length=float(input("Enter petal length:"))
petal_width=float(input("Enter petal width:"))
input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])
predicted_cluster=kmeans.predict(input_data)
print("The input belongs to cluster:",predicted_cluster[0])
