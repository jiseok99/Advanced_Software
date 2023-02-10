import random
import matplotlib.pyplot as plt
import numpy as np  

n = 100000
temp = []
data = []
for _ in range(n):
    temp = random.uniform(0, 4*(10**9))
    data.append(temp)


plt.hist(data)
plt.title(f"Check Uniform Distribution of {n} iterations")
plt.xlabel("Numbers")
plt.xlim([0,4*(10**9)])
plt.ylabel("N of each number")
plt.show()
