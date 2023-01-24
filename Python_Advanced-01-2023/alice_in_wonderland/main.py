n = int(input())
bags_of_tea = 0
matrix = []
alice_position = []
tea_party = False
directions = {
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1),
    'down': (1, 0)
}

for i in range(n):
    matrix.append(input().split())
    if 'A' in matrix[i]:
        alice_position = [i, matrix[i].index('A')]

matrix[alice_position[0]][alice_position[1]] = '*'

while True:
    if bags_of_tea >= 10:
        tea_party = True
        break
    command = input()
    row = directions[command][0] + alice_position[0]
    col = directions[command][1] + alice_position[1]
    if 0 <= row < n and 0 <= col < n:
        alice_position = [row, col]
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            break
        elif matrix[row][col].isdigit():
            bags_of_tea += int(matrix[row][col])
            matrix[row][col] = '*'
        else:
            matrix[row][col] = '*'
    else:
        break

if tea_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for x in matrix:
    print(*x, sep=' ')
