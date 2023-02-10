import random
import matplotlib.pyplot as plt
import numpy as np  
import math

n = 20000
x_list = []
y_list = []
circle_x = []
circle_y = []
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    x_list.append(x)
    y_list.append(y)

    if np.sqrt(x ** 2 + y ** 2) <= 1:  
        circle_x.append(x)  
        circle_y.append(y)  
        
fig = plt.figure(figsize=(10,10),facecolor = 'white')
ax = fig.add_subplot()
plt.scatter(x_list, y_list)
plt.scatter(circle_x, circle_y, c='r')  
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,2.0)
area = len(circle_x) / len(x_list) 

ax.patch.set_facecolor('skyblue')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('center')
ax.spines['right'].set_visible(False)

pi = area * 4
ax.text(-1.9,1.5,f"Number of iteration : {n}\nEstimated pi : {pi}\nReal pi : {round(math.pi, 6)}\nError rate : {round((abs(pi-math.pi)/math.pi)*100,2)}%", c = 'r', backgroundcolor = 'pink')
 
plt.show()
