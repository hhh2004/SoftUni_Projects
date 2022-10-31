vehicles = input().split(">>")
total_taxes = 0

for vehicle in vehicles:
    specs = vehicle.split(" ")
    if specs[0] == "family":
        tax = 50 - int(specs[1]) * 5 + int(specs[2]) // 3000 * 12
    elif specs[0] == "heavyDuty":
        tax = 80 - int(specs[1]) * 8 + int(specs[2]) // 9000 * 14
    elif specs[0] == "sports":
        tax = 100 - int(specs[1]) * 9 + int(specs[2]) // 2000 * 18
    else:
        print("Invalid car type.")
        continue
    total_taxes += tax
    print(f"A {specs[0]} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
