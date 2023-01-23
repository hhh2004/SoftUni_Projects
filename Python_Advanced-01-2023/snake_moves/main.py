rows, columns = map(int, input().split())
text = input()
word_index = 0

for i in range(rows):
    line = []
    for j in range(columns):
        line.append(text[word_index])
        word_index += 1
        if word_index >= len(text):
            word_index = 0
    if i % 2 == 0:
        print(''.join(line))
    else:
        print(''.join(reversed(line)))
