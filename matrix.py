import numpy as np
n=int(input("Enter size of matrix:"))
print(f"Enter {n*n} elements")
element=list(map(float,input().split()))
print("List:",element)
m=np.array(element).reshape(n,n)
print("Matrix:",m)
t_arr=np.transpose(m)
print("Transpose:",t_arr)
t=np.matrix.trace(m)
print("Trace:",t)
d_arr=np.linalg.det(m)
print("Determinant:",d_arr)
i_arr=np.linalg.inv(m)
print("Inverse:",i_arr)


