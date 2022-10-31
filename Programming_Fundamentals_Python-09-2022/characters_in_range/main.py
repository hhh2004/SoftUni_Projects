def char_in_range(char_a, char_b):
    """returns a list of all characters between char_a and char_b on the ASCII table"""
    characters = []
    for i in range(ord(char_a)+1, ord(char_b)):
        characters.append(chr(i))
    return characters


ch_1 = input()
ch_2 = input()
character_list = char_in_range(ch_1, ch_2)
print(" ".join(character_list))
