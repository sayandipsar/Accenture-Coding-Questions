str1 = input("Enter first string    ")
str2 = input("Enter second string   ")
if(len(str1) != len(str2)):
    print('No')
else:
    l = len(str1)
    c = 0
    for i in str1:
        if i in str2:
            c += 1
    if c == l:
        print('Yes')
    else:
        print('No')
