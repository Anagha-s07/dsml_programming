import matplotlib.pyplot as plt
import numpy as np
language=["java","python","php","javascript","c#","c++"]
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.pie(y,labels=language)
plt.title("Popularity of programming language")
plt.show()
