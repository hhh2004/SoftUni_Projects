from string import punctuation as punc

file = open("text.txt", "r")
text = file.readlines()
file.close()
output_file = open("output.txt", "w")
output = []

for i in range(len(text)):
    line = text[i]
    line = line.strip()
    letters = 0
    punctuation = 0
    for char in line:
        if char.isalpha():
            letters += 1
        elif char in punc:
            punctuation += 1
    processed_line = f"Line {i+1}: {line} ({letters})({punctuation})"
    output.append(processed_line)

output_file.write('\n'.join(output))
output_file.close()
