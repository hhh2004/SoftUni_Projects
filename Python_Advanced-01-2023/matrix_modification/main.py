def check_coordinates(comm: list, r, c):
    if 0 <= comm[1] < r and 0 <= comm[2] < c:
        return True
    else:
        return False


def add_matrix(mat, comm):
    mat[comm[1]][comm[2]] += comm[3]
    return


def subtract_matrix(mat, comm):
    mat[comm[1]][comm[2]] -= comm[3]
    return


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
while True:
    command = input().split()
    if command[0] == 'END':
        for x in matrix:
            print(*x, sep=' ')
        break
    else:
        command[1:] = [int(x) for x in command[1:]]
        if not check_coordinates(command, n, len(matrix[0])):
            print('Invalid coordinates')
        elif command[0] == 'Add':
            add_matrix(matrix, command)
        elif command[0] == 'Subtract':
            subtract_matrix(matrix, command)
