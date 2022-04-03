n = int(input("Enter a value  "))
val = 0
x = 2
while(val != n):
    c = 0
    for i in range(1, x+1):
        if x % i == 0:
            c += 1
    if c == 2:
        val += 1
    if val == n:
        break
    x += 1
print(x)
