from itertools import permutations
d = int(input("How many digits    "))
lis = list(input("Enter a number   ").strip())
n = ''
n = n.join(lis)
m = int(n)
perm = list(permutations(lis, d))
store = []
for tuple in perm:
    s = ''.join(tuple)
    store.append(int(s))
store.sort()
print(store[store.index(m)+1])
