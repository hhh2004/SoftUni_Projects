deck = input().split(" ")
shuffles = int(input())

for _ in range(shuffles):
    new_deck = []
    for i in range(len(deck)//2):
        new_deck.append(deck[i])
        new_deck.append(deck[len(deck)//2+i])
    deck = new_deck

print(deck)
