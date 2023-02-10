import random
import numpy as np  
import sys


n = 100
first = []
second = []
count = 0
print('=====================================================================================')
print("\033[31m* 두 주사위의 합이 8인 경우에는 cyan 색의 음영이 들어가있음 * \033[0m", end =' ')
for i in range(n):
    first= random.randint(1,6)
    second = (random.randint(1,6))

    if i % 4 == 0:
      print(end = '\n')

    if first + second == 8:
       count += 1
       print( '\033[33m\033[46mtry','{' ':2d}'.format(i),':',first,second,'\033[0m',end = '')
    else:
       print('try','{' ':2d}'.format(i),':',first,second, end = ' ')
print('\n')
act = 5 / 36
cal = count / n
print('\033[31m실제 값 : ',round(act, 6))
print('\033[31m계산된 값 : ',cal )
print('오차율 : ',abs(((cal - act)/act)*100),'%','\033[0m')

print('=====================================================================================')

