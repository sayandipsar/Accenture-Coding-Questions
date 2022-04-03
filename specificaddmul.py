arr = list(map(int, input().split()))
s = ""
for i in range(len(arr)):
    addg = 0
    adds = 0
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            addg += arr[j]
        elif arr[j] < arr[i]:
            adds += arr[j]
    mul = addg*adds
    if s == "":
        s += str(mul)
    else:
        s += " "+str(mul)
print(s)
