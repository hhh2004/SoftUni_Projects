numbers = input().split(", ")
beggars = int(input())
earnings = []
for i in range(beggars):
    earnings.append(0)

for i in range(len(numbers)):
    beggar = i % beggars
    earnings[beggar] += int(numbers[i])

print(earnings)
