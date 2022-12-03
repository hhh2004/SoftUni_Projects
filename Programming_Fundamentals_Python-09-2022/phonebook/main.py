phonebook = {}
while True:
    entry = input().split('-')
    if len(entry) != 2:
        searches = int(entry[0])
        break
    phonebook[entry[0]] = entry[1]
for _ in range(searches):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
