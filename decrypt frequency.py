# Decode and find the character in the sting available
s = list(input().strip())
n = int(input())
print(s)
sums = 0
flag = 0
for i in range(1, len(s), 2):
    x = int(s[i])
    sums += x
    if sums >= n:
        flag = 1
        break
if flag == 1:
    print(s[i-1])
else:
    print('Not found')
