import matplotlib.pyplot as plt
import numpy as np
language=["java","python","php","javascript","c#","c++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(language,popularity)
plt.xlabel("programming language")
plt.ylabel("popularity")
plt.title("popularity of programming language")
plt.show()
