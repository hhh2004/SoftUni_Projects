from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))
presents = {
    'Bicycle': 0,
    'Doll': 0,
    'Teddy bear': 0,
    'Wooden train': 0
}

levels = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while magic_level and materials:
    product = materials[-1] * magic_level[0]
    if product in levels.keys():
        presents[levels[product]] += 1
        materials.pop()
        magic_level.popleft()
    elif product < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif product > 0:
        magic_level.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
    elif materials[-1] == 0:
        materials.pop()
    else:
        magic_level.popleft()

if (presents['Bicycle'] and presents['Teddy bear']) or (presents['Doll'] and presents['Wooden train']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
elif magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for k, v in presents.items():
    if v != 0:
        print(f"{k}: {v}")
