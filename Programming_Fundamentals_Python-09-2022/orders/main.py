orders = {}
while True:
    command = input().split(' ')
    if command[0] == "buy" and len(command) == 1:
        break

    if command[0] in orders.keys():
        orders[command[0]][0] = float(command[1])
        orders[command[0]][1] += int(command[2])
    else:
        orders[command[0]] = []
        orders[command[0]].append(float(command[1]))
        orders[command[0]].append(int(command[2]))

for order in orders.keys():
    print(f"{order} -> {(orders[order][0]*orders[order][1]):.2f}")

