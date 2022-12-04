animals = {}
areas_hungy = {}

while True:
    command = input()
    if command == "EndDay":
        break
    else:
        command = command.split(': ')
    if command[0] == "Add":
        command[1] = command[1].split('-')
        if command[1][0] in animals.keys():
            animals[command[1][0]][0] += int(command[1][1])
        else:
            animals[command[1][0]] = []
            animals[command[1][0]].append(int(command[1][1]))
            animals[command[1][0]].append(command[1][2])
    elif command[0] == "Feed":
        command[1] = command[1].split('-')
        if command[1][0] in animals.keys():
            animals[command[1][0]][0] -= int(command[1][1])
            if animals[command[1][0]][0] <= 0:
                animals.pop(command[1][0])
                print(f"{command[1][0]} was successfully fed")

print("Animals:")
for animal in animals.keys():
    print(f" {animal} -> {animals[animal][0]}g")
    if animals[animal][0] > 0:
        if animals[animal][1] in areas_hungy.keys():
            areas_hungy[animals[animal][1]] += 1
        else:
            areas_hungy[animals[animal][1]] = 1
print("Areas with hungry animals:")
for area in areas_hungy:
    print(f"{area}: {areas_hungy[area]}")
