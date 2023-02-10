import time

n = int(input("N : "))
print("각 나라별 필요 노력을 입력해주세요")
cities = [list(map(int, input().split())) for _ in range(n)]
VISITED_ALL = (1 << n) - 1

INF = float('inf')
cache = [[INF] * (1 << n) for _ in range(n)]

idx = 1

def find_path(last, visited):
    if visited == (1 << n) - 1:     
        if cities[last][0]:            
            return cities[last][0]
        else:                      
            return INF

    if cache[last][visited] is not INF:      
        return cache[last][visited]

    for i in range(1, n):           
        if not cities[last][i]:         
            continue
        if visited & (1 << i):     
            continue

        cache[last][visited] = min(cache[last][visited], find_path(i, visited | (1 << i)) + cities[last][i])
    return cache[last][visited]

start = time.time()
print(f"정답은 {find_path(0, 1 << 0)}이고, 걸린시간은 {time.time()-start}입니다.")
