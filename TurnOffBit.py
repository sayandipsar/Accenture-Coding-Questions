n = int(input())
k = int(input())
x = ""
while n > 0:
    x += str(n % 2)
    n = n//2
print(x)
s = ''
ind = len(x)-k
for i in range(len(x)):
    if i == ind:
        s += '0'
    else:
        s += x[i]
m = 0
l = len(s)
for i in range(l):
    if s[i] == '1':
        m += 2**(l-i-1)
print(m)
