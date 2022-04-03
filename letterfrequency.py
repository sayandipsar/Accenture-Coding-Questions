s1 = list(input().strip())
s2 = list(set(s1))
s2.sort()
s = ''
for i in s2:
    s += str(i)+str(s1.count(i))
print(s)
