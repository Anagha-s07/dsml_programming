import matplotlib.pyplot as plt
import numpy as np
maths=[82,92,80,89,100,80,60,100,80,34]
science=[35,79,79,48,100,88,32,45,20,30]
plt.scatter(maths,science,color="green")
plt.xlim(10,100)
plt.ylim(10,100)
plt.xlabel("mathematics")
plt.ylabel("science")
plt.title("scatter plot")
plt.show()
