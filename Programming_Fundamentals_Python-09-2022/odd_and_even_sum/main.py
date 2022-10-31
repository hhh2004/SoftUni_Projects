def odd_and_even_sum(number):
    digits = list(map(int, number))
    odd_total = 0
    even_total = 0
    for n in digits:
        if n % 2 == 0:
            even_total += n
        else:
            odd_total += n
    return f"Odd sum = {odd_total}, Even sum = {even_total}"


print(odd_and_even_sum(input()))
