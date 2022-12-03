items = {"shards": 0, "fragments": 0, "motes": 0}
legendary_obtained = False
while not legendary_obtained:
    entry = input().split(' ')

    for i in range(0, len(entry), 2):
        if entry[i+1].lower() in items.keys():
            items[entry[i+1].lower()] += int(entry[i])
        else:
            items[entry[i+1].lower()] = int(entry[i])

        if items["shards"] >= 250:
            items["shards"] -= 250
            print("Shadowmourne obtained!")
            legendary_obtained = True
            break
        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            print("Valanyr obtained!")
            legendary_obtained = True
            break
        elif items["motes"] >= 250:
            items["motes"] -= 250
            print("Dragonwrath obtained!")
            legendary_obtained = True
            break

print(f"shards: {items['shards']}")
print(f"fragments: {items['fragments']}")
print(f"motes: {items['motes']}")
items.pop("shards")
items.pop("fragments")
items.pop("motes")

for item in items.keys():
    print(f"{item}: {items[item]}")
