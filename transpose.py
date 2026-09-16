import numpy as np
a=input("enter first element:")
b=input("enter second element:")
c=input("enter third element:")
d=input("enter fourth element:")
arr=np.array([[int (a),int (b)],[int (c),int (d)]])
print("Array:",arr)
tra_arr=np.transpose(arr)
print("Transpose:",tra_arr)
