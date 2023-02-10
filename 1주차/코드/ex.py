import random
import matplotlib.pyplot as plt
import numpy as np  

n = 3000
x_list = []
y_list = []
circle_x = []
circle_y = []
for _ in range(n):
    x = random.random()
    y = random.random()
    x_list.append(x)
    y_list.append(y)

    if np.sqrt(x ** 2 + y ** 2) <= 1:  
        circle_x.append(x)  
        circle_y.append(y)  
        
plt.figure(figsize=(10,10))
plt.scatter(x_list, y_list)
plt.scatter(circle_x, circle_y, c='r')  
area = len(circle_x) / len(x_list)  
pi = area * 4
plt.title(f"n={n}, π≈{pi}")  
plt.show()
