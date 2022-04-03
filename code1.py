
# from itertools import combinations, permutations
# minimum penalty
n = int(input())
arr = list(map(int, input().split()))
# arr.sort()
s = 0
for i in range(len(arr)-1):
    s += abs(arr[i]-arr[i+1])
print(s)
# perm = combinations(arr, 2)
# for i in perm:
#     x = 0
#     m = list(i)
#     print(m)
#     for j in m:
#         x += j
#     print(x)
