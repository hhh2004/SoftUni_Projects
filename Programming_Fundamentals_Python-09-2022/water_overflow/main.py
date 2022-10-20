n = int(input())
capacity = 255
total = 0
for i in range(n):
    water = int(input())
    if total+water > capacity:
        print("Insufficient capacity!")
    else:
        total += water
print(total)
