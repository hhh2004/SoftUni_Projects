n_lines = int(input())
elements = set()

for _ in range(n_lines):
    line = input().split()
    for el in line:
        elements.add(el)

print(*elements, sep='\n')
