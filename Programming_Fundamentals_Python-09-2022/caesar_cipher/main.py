text = input()
encrypted_text = []
for char in text:
    encrypted_text.append(chr(ord(char)+3))
encrypted_text = ''.join(encrypted_text)
print(encrypted_text)
