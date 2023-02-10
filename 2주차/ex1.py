from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
width =  1.0
height = 1.0
pointNumber = 25
points = np.zeros((pointNumber, 2)) 
points[:, 0] = np.random.uniform(0, width, pointNumber) 
points[:, 1] = np.random.uniform(0, height, pointNumber)
tri = Delaunay(points)
center = np.sum(points[tri.simplices], axis=1)/3.0 

color = []
for index, sim in enumerate(points[tri.simplices]):
    cx, cy = center[index][0], center[index][1]
    x1, y1 = sim[0][0], sim[0][1]
    x2, y2 = sim[1][0], sim[1][1]
    x3, y3 = sim[2][0], sim[2][1]

plt.figure(figsize=(10, 10)) 
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.tick_params(labelbottom='off', labelleft='off', left='off', right='off', bottom='off', top='off') 
ax = plt.gca() 
plt.scatter(points[:,0],points[:,1], color='black')
plt.show()
