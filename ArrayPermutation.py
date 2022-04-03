lis = list(map(int, input().split()))
print(lis)
s = []
for i in lis:
    n = i
    while(n > 0):
        r = n % 10
        s.append(str(r))
        n = n//10
s.sort()
s.reverse()
string = "".join(s)

print(string)
