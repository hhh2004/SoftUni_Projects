resources = {}
while True:
    material = input()
    if material == "stop":
        break
    quantity = input()
    if quantity == "stop":
        break
    else:
        quantity = int(quantity)
    if material in resources.keys():
        resources[material] += quantity
    else:
        resources[material] = quantity
for key, value in resources.items():
    print(f"{key} -> {value}")
