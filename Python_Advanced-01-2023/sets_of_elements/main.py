lengths = tuple(map(int, input().split()))

first_set = {int(input()) for _ in range(lengths[0])}
second_set = {int(input()) for _ in range(lengths[1])}
output_set = first_set & second_set
print(*output_set, sep='\n')

