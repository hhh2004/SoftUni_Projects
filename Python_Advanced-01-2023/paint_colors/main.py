from collections import deque

substrings = deque(input().split())
colors = ('red', 'yellow', 'blue', 'orange', 'purple', 'green')
secondary_colors = {
    'orange': {'yellow', 'red'},
    'green': {'yellow', 'blue'},
    'purple': {'blue', 'red'}
}
found_colours = []

while substrings:
    if len(substrings) > 1:
        if substrings[0] + substrings[-1] in colors:
            found_colours.append(substrings.popleft() + substrings.pop())
        elif substrings[-1] + substrings[0] in colors:
            found_colours.append(substrings.pop() + substrings.popleft())
        else:
            if len(substrings[0]) > 1:
                str_to_insert = substrings.popleft()[:-1]
                substrings.insert(len(substrings) // 2, str_to_insert)
            else:
                substrings.popleft()
            if len(substrings[-1]) > 1:
                str_to_insert = substrings.pop()[:-1]
                substrings.insert(len(substrings) // 2, str_to_insert)
            else:
                substrings.pop()
    elif substrings[0] in colors:
        found_colours.append(substrings.pop())
    elif len(substrings[0]) > 1:
        substrings[0] = substrings[0][:-1]
    else:
        substrings.pop()

for color in found_colours:
    if color in secondary_colors.keys() and not secondary_colors[color].issubset(found_colours):
        found_colours.remove(color)

print(found_colours)
