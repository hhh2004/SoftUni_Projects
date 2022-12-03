text = input()
chars = {}
for char in text:
    if char == ' ':
        continue
    elif char in chars:
        chars[char] += 1
    else:
        chars[char] = 1
for key, value in chars.items():
    print(f"{key} -> {value}")
