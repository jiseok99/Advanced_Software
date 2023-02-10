N = int(input())
times = []
for n in range(N) :
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

answer = ''
end = 0

for t in times :
   if end <= t[0]:
       answer += str(t[0]) + ' ' + str(t[1])+ ' '
       end = t[1]
       
        
       

print(times)
print(answer)
