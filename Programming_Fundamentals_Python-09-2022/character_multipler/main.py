strings = input().split(' ')
total = 0
for i in range(min(len(strings[0]), len(strings[1]))):
    total += ord(strings[0][i]) * ord(strings[1][i])
for char in max(strings[0], strings[1], key=len)[i+1:]:
    total += ord(char)
print(total)
