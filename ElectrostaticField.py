lis = list(map(int, input().split()))
np = input()
n = int(input())
charge = 0
for i in range(n):
    if np[i] == 'p':
        charge += lis[i]
    elif np[i] == 'n':
        charge += -(lis[i])
charge = charge*100
print(charge)
