words = input().split(' ')
message = []
for word in words:
    deciphered_word = []
    first_letter = []
    rest_of_word = []
    for char in word:
        if char.isnumeric():
            first_letter.append(char)
        else:
            rest_of_word.append(char)
    first_letter = chr(int(''.join(first_letter)))
    last_letter = rest_of_word[0]
    rest_of_word[0] = rest_of_word[-1]
    rest_of_word[-1] = last_letter
    deciphered_word = first_letter + ''.join(rest_of_word)
    message.append(deciphered_word)
print(' '.join(message))
