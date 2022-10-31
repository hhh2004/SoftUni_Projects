cards = input().split(", ")
total_commands = int(input())

for _ in range(total_commands):
    command = input().split(", ")
    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            cards.append(command[1])
            print("Card successfully added")
    elif command[0] == "Remove":
        if command[1] in cards:
            cards.remove(command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        if len(cards) > int(command[1]) >= 0:
            cards.pop(int(command[1]))
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        if len(cards) > int(command[1]) >= 0:
            if command[2] in cards:
                print("Card is already added")
            else:
                cards.insert(int(command[1]), command[2])
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(cards))

