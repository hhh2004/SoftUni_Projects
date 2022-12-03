text = input()
edited_text = [text[0]]
for i in range(1, len(text)):
    if text[i] != text[i-1]:
        edited_text.append(text[i])
print(''.join(edited_text))
