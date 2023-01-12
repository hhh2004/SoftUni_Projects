from collections import deque

food = int(input())
orders = deque(map(int, input().split(' ')))

print(max(orders))
while orders:
    if orders[0] <= food:
        order = orders.popleft()
        food -= order
    else:
        print("Orders left: ", end='')
        print(*orders, sep=' ')
        break
else:
    print('Orders complete')
