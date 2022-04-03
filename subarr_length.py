n = int(input())
lis = list(map(int, input().split(',')))
n1 = lis.count(0)
n2 = lis.count(1)
m = (min(n1, n2))*2
print(m)
