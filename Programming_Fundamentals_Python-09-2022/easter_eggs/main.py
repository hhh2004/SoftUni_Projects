import re

text = input()
regex1 = r"[@#]+[a-z]{3,}[@#]+[^0-9a-zA-Z]*/+[0-9]+/+"
regex_colour = r"[a-z]{3,}"
regex_amount = r"\d+"
matches = re.findall(regex1, text)
colours, amounts = [], []
for match in matches:
    colours.append(re.findall(regex_colour, match)[0])
    amounts.append(re.findall(regex_amount, match)[0])
for i in range(len(colours)):
    print(f"You found {amounts[i]} {colours[i]} eggs!")
