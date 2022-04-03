lis = list(map(int, input().split()))
n = len(lis)
s = 0
for i in range(n):
    c = 0
    for j in range(i+1, n):
        if lis[i] > lis[j]:
            c += 1
    if c == n-i-1:
        s += 1
print(s)
