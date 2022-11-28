from math import ceil

numbers = list(map(int, input().split(', ')))
grouped_numbers = [[] for _ in range((ceil(max(numbers)/10)))]
for num in numbers:
    grouped_numbers[ceil(num/10)-1].append(num)
for i in range(len(grouped_numbers)):
    print(f"Group of {(i+1)*10}'s: {grouped_numbers[i]}")
