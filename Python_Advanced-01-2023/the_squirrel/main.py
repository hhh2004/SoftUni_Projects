hazelnuts = 0
size = int(input())
directions = input().split(', ')
field = []
for _ in range(size):
    field.append(list(input()))

direction_dict = {
    'left': (0, -1),
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0)
}

position = []

for x in range(size):
    for y in range(size):
        if field[x][y] == 's':
            position = [x, y]
            break
    else:
        continue
    break

for direction in directions:
    new_x = position[0]+direction_dict[direction][0]
    new_y = position[1]+direction_dict[direction][1]
    if new_x < 0 or new_x >= size or new_y < 0 or new_y >= size:
        print('The squirrel is out of the field.')
        break
    new_thing = field[new_x][new_y]
    if new_thing == 'h':
        hazelnuts += 1
        field[new_x][new_y] = '*'
    elif new_thing == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break
    position = [new_x, new_y]
else:
    if hazelnuts >= 3:
        print('Good job! You have collected all hazelnuts!')
    else:
        print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts}')
