n = int(input("How many elements  "))
lis = list(map(int, input().split()))
lis = list(set(lis))
lis.sort()
if len(lis) >= 2:
    print(lis[len(lis)-2])
else:
    print(-1)
