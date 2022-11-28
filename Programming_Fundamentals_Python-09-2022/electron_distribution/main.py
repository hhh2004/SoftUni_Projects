total_electrons = int(input())
shells = []
i = 0
while True:
    electrons = (i+1) ** 2 * 2
    if total_electrons > electrons:
        total_electrons -= electrons
        shells.append(electrons)
    else:
        shells.append(total_electrons)
        break
    i += 1
print(shells)
