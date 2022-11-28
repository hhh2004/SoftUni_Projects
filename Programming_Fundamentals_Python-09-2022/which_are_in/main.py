first_sequence = input().split(', ')
second_sequence = input().split(', ')

substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
print(substrings)
