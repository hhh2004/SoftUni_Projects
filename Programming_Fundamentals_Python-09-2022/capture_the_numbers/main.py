import re
matches = []
search_pattern = r"\d+"
line = input()
while line:
    matches.extend(re.findall(search_pattern, line))
    line = input()
print(' '.join(matches))
