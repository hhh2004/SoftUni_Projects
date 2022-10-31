numbers = input().split(", ")
for num in numbers:
    is_palindrome = True
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            is_palindrome = False
            break
    print(is_palindrome)
