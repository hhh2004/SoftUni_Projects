n = int(input())
field = []
bunny_pos = []
best_path = []
best_direction = None
max_eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(n):
    field.append(input().split())
    if 'B' in field[i]:
        bunny_pos = [i, field[i].index('B')]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n and field[row][col] != 'X':
        collected_eggs += int(field[row][col])
        path.append([row, col])
        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
