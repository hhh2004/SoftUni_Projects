from collections import deque
from copy import deepcopy

n_pumps = int(input())
fuel = 0
pumps = deque()

for i in range(n_pumps):  # pumps[0] - fuel from station, [1] - distance to next station, [2] - index of station
    pumps.append(list(map(int, input().split(' '))))
    pumps[i].append(i)

current_pumps = deepcopy(pumps)

while current_pumps:
    fuel += current_pumps[0][0]
    fuel -= current_pumps[0][1]
    if fuel < 0:
        fuel = 0
        pumps.rotate(-1)
        current_pumps = deepcopy(pumps)
        continue
    else:
        current_pumps.popleft()

print(pumps[0][2])
