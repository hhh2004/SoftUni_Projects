rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
squares = 0

for i in range(rows-1):
    for j in range(columns-1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            squares += 1

print(squares)
