from collections import deque


def prod(x: list):
    product = 1
    for i in x:
        product *= i
    return product


expr = deque(input().split())
numbers = list()
operations = {
    '+': lambda x: sum(x),
    '-': lambda x: x[0] - sum(x[1:]),
    '*': lambda x: prod(x),
    '/': lambda x: x[0] // prod(x[1:])
}

while expr:
    char = expr[0]
    expr.popleft()
    if char in ('+', '-', '*', '/'):
        num = operations[char](numbers)
        numbers.clear()
        numbers.append(num)
    else:
        num = int(char)
        numbers.append(num)

print(numbers[0])
