import matplotlib.pyplot as plt
import numpy as np
score=[55,62,67,71,75,78,79,80,81,83,84,85,87,88,89,90,91,92,93,95,96,97,98,99,100,65,73,82,88,91]
plt.hist(score,bins=5,color='blue',edgecolor='black')
plt.xlabel("Score")
plt.ylabel("no.of.students")
plt.show()
