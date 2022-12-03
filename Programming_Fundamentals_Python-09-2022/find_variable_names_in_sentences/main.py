import re

text = input()
matches = [match.group(1) for match in re.finditer(r"\b_([a-zA-Z\d]+\b)", text)]
print(','.join(matches))
