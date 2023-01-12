clothes = list(map(int, input().split()))
rack_space = int(input())
racks = 1
current_rack_space = rack_space
while clothes:
    garment = clothes.pop()
    if garment <= current_rack_space:
        current_rack_space -= garment
    else:
        racks += 1
        current_rack_space = rack_space - garment

print(racks)
