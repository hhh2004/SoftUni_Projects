data = reversed(input().split('|'))
flattened_list = []
for x in data:
    flattened_list.extend(x.split())
print(*flattened_list, sep=' ')
