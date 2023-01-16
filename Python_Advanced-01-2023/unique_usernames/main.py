n_names = int(input())
names = set()

for _ in range(n_names):
    names.add(input())

print(*names, sep='\n')
