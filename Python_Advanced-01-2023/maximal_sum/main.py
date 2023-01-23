rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
max_sum = None
max_matrix = None
for i in range(rows - 2):
    for j in range(columns - 2):
        sub_matrix = [x[j:j+3] for x in matrix[i:i+3]]
        matrix_sum = sum([sum(x) for x in sub_matrix])
        if (max_sum is not None and matrix_sum > max_sum) or max_sum is None:
            max_sum = matrix_sum
            max_matrix = sub_matrix

print(f"Sum = {max_sum}")
for x in max_matrix:
    print(*x, sep=' ')
