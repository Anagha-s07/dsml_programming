import matplotlib.pyplot as plt
import numpy as np
x =np.array([1,2,4,6])
y =np.array([3,7,9,10])
y1 =np.array([4,5,8,11])
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.title("plot of two lines")
plt.plot(x,y,label="Line1",color="green",marker="o")
plt.plot(x,y1,label="Line2",color="red",marker="o")
plt.legend()
plt.show()

