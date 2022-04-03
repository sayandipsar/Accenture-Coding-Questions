lis1=list(map(int,input().split()))
lis2=list(map(int,input().split()))
s=0
for i in lis1:
    if i not in lis2:
        s+=i 
for j in lis2:
    if j not in lis1:
        s+=j 
print(s)