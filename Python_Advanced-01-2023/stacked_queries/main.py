stack = []

map_functions = {
    '1': lambda x: stack.append(int(x.split()[1])),
    '2': lambda x: stack.pop() if stack else None,
    '3': lambda x: print(max(stack)) if stack else None,
    '4': lambda x: print(min(stack)) if stack else None
}

n = int(input())
for _ in range(n):
    command = input()
    map_functions[command[0]](command)

stack.reverse()
print(*stack, sep=', ')
