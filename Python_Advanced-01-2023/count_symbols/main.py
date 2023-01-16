text = input()
letters = dict()
for ch in text:
    if ch in letters.keys():
        letters[ch] += 1
    else:
        letters[ch] = 1
sorted_chars = sorted(letters.keys())
for ch in sorted_chars:
    print(f"{ch}: {letters[ch]} time/s")
