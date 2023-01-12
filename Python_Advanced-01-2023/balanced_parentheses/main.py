parentheses = input()
stack_parentheses = []

parentheses_map = {
    '(': ')',
    '[': ']',
    '{': '}'
}

for ch in parentheses:
    if ch in ('(', '[', '{'):
        stack_parentheses.append(ch)
    elif stack_parentheses and ch == parentheses_map[stack_parentheses.pop()]:
        pass
    else:
        print('NO')
        break
else:
    print('YES')
