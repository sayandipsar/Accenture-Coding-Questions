row = int(input("How many row   "))
col = int(input("How many column    "))
lis = list(map(int, input().split(',')))
matrix = []
l = len(lis)
i = 0
while(i < l):
    mat = lis[i:i+col]
    matrix.append(mat)
    i = i+row
# print(matrix)
maxrow = 0
valrow = 0
for i in range(row):
    for j in range(col):
        valrow += matrix[i][j]
    if valrow > maxrow:
        maxrow = valrow
    valrow = 0

maxcol = 0
valcol = 0
for x in range(row):
    for y in range(col):
        valcol += matrix[y][x]
    if valcol > maxcol:
        maxcol = valcol
    valcol = 0
# print("Maxrow= "+str(maxrow)+" and MAxcol= "+str(maxcol))

print(maxrow+maxcol)
