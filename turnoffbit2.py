n=int(input())
k=int(input())
s=0
while(n>0):
    r=n%2
    s=s*10+r 
    n=n//2
l=len(str(s))-k

m1=str(s)
m=""
for i in range(-1,-(len(m1)+1),-1):
    m+=m1[i]
sen=""
for i in range(len(m)):
    if i==l:
        sen+='0'
    else:
        sen+=m[i]
print(sen)
x=""
for i in range(-1,-(len(sen)+1),-1):
    x+=sen[i]

res=0
for i in range(len(x)):
    if x[i]=='1':
        res+=2**i
print(res)
