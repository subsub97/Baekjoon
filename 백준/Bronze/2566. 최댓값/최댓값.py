matrix = []
max = -1
for _ in range(9):
    matrix.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max:
            global row
            global col
            max = matrix[i][j]
            row = i+1
            col = j+1
print(max)
print(row,col)