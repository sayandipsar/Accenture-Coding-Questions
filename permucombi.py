from itertools import permutations, combinations
lis = list(map(int, input("Enter a number   ").strip()))
perm = permutations(lis, 2)
# print(perm)
for i in perm:
    print(i)
