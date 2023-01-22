from collections import deque

chocolates = deque(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif chocolates[-1] <= 0:
        chocolates.pop()
        continue
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    elif chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")


