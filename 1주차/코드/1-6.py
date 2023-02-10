import random
import matplotlib.pyplot as plt
import numpy as np  
import math

n = 10000
result = []
c1 = 0
c2 = 0

for _ in range(n):
  temp = random.triangular(1,9,3)
  aw = random.randint(0,1)
  if aw == 1:
    pro = random.uniform(1.25,1.75)
    temp = temp * pro
  if temp > 6:
    c2 +=1
  else:
    c1 +=1
  result.append(temp)

c1 = round((c1 / n) * 100,1)
c2 = round((c2 / n) * 100,1)

x = ['Probability : less or equal to 600 million won', 'Probability : greater to 600 million won']
y = [c1, c2]

plt.figure(figsize=(12,10))
bar = plt.bar(x, y, color = ['tab:blue' ,'orange'])

for i in bar:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, '%.1f%%' % height, ha='center', va='bottom')

plt.gca().axes.yaxis.set_visible(False)
plt.show()

print("6억원 이하의 매출을 얻을 확률 :",'\033[31m',c1, '\033[0m')
print("6억원 초과의 매출을 얻을 확률 :",'\033[34m',c2, '\033[0m')
