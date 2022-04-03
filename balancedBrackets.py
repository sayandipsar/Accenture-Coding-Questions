s = input("Enter a string ")
arr = list(s.strip())
brr = []
for i in range(len(arr)):
    brr.append(arr[i])
    top = len(brr)-1
    if (top >= 1) and brr[top] == '}' and brr[top-1] == '{':
        brr.pop()
        brr.pop()
# print(brr)
if len(brr) == 0:
    print("Brackets are balanced")
else:
    print("Brackets are not balanced")
