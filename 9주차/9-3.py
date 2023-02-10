n = int(input("N : "))
print("수열을 입력해주세요 : ")
a = list(map(int, input().split()))

sum = [a[0]]

for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i+1], a[i+1]))
    print(sum)
    

print(f"정답은 {max(sum)}입니다.")
