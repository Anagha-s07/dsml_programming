import numpy as np
a=input("enter first element:")
b=input("enter second element:")
c=input("enter third element:")
d=input("enter fourth element:")
arr=np.array([[int (a),int (b)],[int (c),int (d)]])
print("Array:",arr)
det_arr=np.linalg.det(arr)
print("Determinant:",det_arr)
