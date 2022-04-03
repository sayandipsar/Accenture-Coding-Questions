a = input()
b = input()
c = ord(b)-ord(a)
if(ord(b)+c) <= 122:
    print(chr(ord(b)+c))
elif(ord(b)+c) > 122:
    x = 97+ord(b)+c-122
    print(chr(x))

# print(ord(a))
