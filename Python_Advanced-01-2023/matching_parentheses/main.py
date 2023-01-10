expression = input()
parentheses = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses.append(i)
    elif expression[i] == ')':
        expr_start = parentheses.pop()
        for j in range(expr_start, i+1):
            print(expression[j], end="")
        print()

