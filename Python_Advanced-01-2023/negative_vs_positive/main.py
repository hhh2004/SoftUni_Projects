nums = map(int, input().split())
negative_sum = 0
positive_sum = 0

for n in nums:
    if n > 0:
        positive_sum += n
    else:
        negative_sum += n

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
