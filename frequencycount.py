string = list(input().strip())
string.sort()
set = set(string)
s = ""
for i in set:
    c = string.count(i)
    s += i+str(c)
print(s)
