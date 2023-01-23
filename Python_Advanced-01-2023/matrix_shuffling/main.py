def command_checker(comm, r, c):
    comm = comm.split()
    if comm[0] == 'swap' and len(comm) == 5 and 0 <= int(comm[1]) < r and 0 <= int(comm[2]) < c \
            and 0 <= int(comm[3]) < r and 0 <= int(comm[4]) < c:
        return True
    return False


def swap(comm, mat):
    comm = [int(x) for x in comm.split()[1:]]
    v1 = mat[comm[0]][comm[1]]
    mat[comm[0]][comm[1]] = mat[comm[2]][comm[3]]
    mat[comm[2]][comm[3]] = v1


rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
while True:
    command = input()
    if command == 'END':
        break
    elif command_checker(command, rows, columns):
        swap(command, matrix)
        print(*[' '.join(map(str, x)) for x in matrix], sep='\n')
    else:
        print("Invalid input!")
