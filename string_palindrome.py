str1 = input()
s = ''
for i in range(-1, -(len(str1)+1), -1):
    s += str1[i]
if(s == str1):
    print(1)
else:
    print(0)
print(s)
