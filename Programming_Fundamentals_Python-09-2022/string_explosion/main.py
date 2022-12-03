text = input()
exploded_text = []
explosion_strength = 0
for i in range(len(text)):
    if text[i] == '>':
        explosion_strength += int(text[i+1])
        exploded_text.append('>')
    elif explosion_strength > 0:
        explosion_strength -= 1
    else:
        exploded_text.append(text[i])
print(''.join(exploded_text))
