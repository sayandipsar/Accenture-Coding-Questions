import math
a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c 
e=math.sqrt(abs(d))
x=-b/(2*a)
y=e/(2*a)
if(d>=0):
    print(str(x+y)+','+str(x-y))
else:
    print(str(x)+'+i'+str(y)+','+str(x)+'-i'+str(y))