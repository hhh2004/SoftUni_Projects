odd_nums = set()
even_nums = set()

for i in range(1, int(input()) + 1):
    ascii_sum = sum(ord(ch) for ch in input()) // i
    if ascii_sum % 2:
        odd_nums.add(ascii_sum)
    else:
        even_nums.add(ascii_sum)

odd_sum = sum(odd_nums)
even_sum = sum(even_nums)
if odd_sum == even_sum:
    print(*(odd_nums | even_nums), sep=', ')
elif odd_sum > even_sum:
    print(*(odd_nums - even_nums), sep=', ')
else:
    print(*(odd_nums ^ even_nums), sep=', ')
