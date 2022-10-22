nums = input().split(" ")
to_remove = int(input())

for i in range(len(nums)):
    nums[i] = int(nums[i])
sorted_nums = sorted(nums)

for i in range(to_remove):
    nums.remove(sorted_nums[i])

for i in range(len(nums)-1):
    print(nums[i], end=", ")
print(nums[-1])
