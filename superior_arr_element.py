lis = list(map(int, input().split()))
n = len(lis)
s = 0
for i in range(n-1):
    lis2 = lis[i+1:]
    m = max(lis2)
    if lis[i] > m:
        s += 1
print(s)
