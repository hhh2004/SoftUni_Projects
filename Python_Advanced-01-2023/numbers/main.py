seq1 = set(map(int, input().split()))
seq2 = set(map(int, input().split()))
n = int(input())

commands = {
    'Add First': lambda x: [seq1.add(num) for num in x],
    'Add Second': lambda x: [seq2.add(num) for num in x],
    'Remove First': lambda x: [seq1.discard(num) for num in x],
    'Remove Second': lambda x: [seq2.discard(num) for num in x],
    'Check Subset': lambda: print(seq1.issubset(seq2) or seq2.issubset(seq1))
}

for _ in range(n):
    entered_command = input().split()
    command = ' '.join(entered_command[:2])
    if len(entered_command) > 2:
        nums = list(map(int, entered_command[2:]))
        commands[command](nums)
    else:
        commands[command]()

final_seq1 = sorted(list(seq1))
final_seq2 = sorted(list(seq2))
print(*final_seq1, sep=', ')
print(*final_seq2, sep=', ')
