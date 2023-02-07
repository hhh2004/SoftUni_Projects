file = open("text.txt", "r")
text = file.readlines()
file.close()
output = []
replacements = (
    ("-", "@"),
    (",", "@"),
    (".", "@"),
    ("?", "@"),
    ("!", "@"),
)

for i in range(0, len(text), 2):
    line = text[i]
    for old, new in replacements:
        line = line.replace(old, new)
    line = line.split()
    line.reverse()
    output.append(' '.join(line))

print(*output, sep='\n')
