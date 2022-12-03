import re

text = input()
search_word = input()
regex = r"{}\b".format(search_word)
matches = re.findall(regex, text, re.IGNORECASE)
print(len(matches))
