import matplotlib.pyplot as plt 

global rand
rand = 1

def lcg():
    a = 214013
    c = 2531011
    m = 2**32
    global rand
    rand = (a*rand + c) % m
    return rand

n = 10000
data = []
for i in range(n):
    data.append(lcg())

  
plt.hist(data)
plt.title(f"Check Uniform Distribution of {n} iterations")
plt.xlabel("Numbers")
plt.xlim([0,4*(10**9)])
plt.ylabel("N of each number")
plt.show()
