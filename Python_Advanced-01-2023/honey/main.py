from collections import deque

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())
honey = 0

operations = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y
}

while bees and nectar:
    if bees[0] <= nectar[-1]:
        if nectar[-1] != 0 or symbols[0] != '/':
            honey += abs(operations[symbols.popleft()](bees.popleft(), nectar.pop()))
        else:
            symbols.popleft()
            bees.popleft()
            nectar.pop()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
elif nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
