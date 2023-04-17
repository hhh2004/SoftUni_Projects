from collections import deque

time_sequence = deque(map(int, input().split()))
task_sequence = list(map(int, input().split()))
rubber_duckies = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while len(task_sequence) > 0:
    tasks_time = time_sequence[0] * task_sequence[-1]
    if tasks_time <= 60:
        rubber_duckies['Darth Vader Ducky'] += 1
        time_sequence.popleft()
        task_sequence.pop()
    elif tasks_time <= 120:
        rubber_duckies['Thor Ducky'] += 1
        time_sequence.popleft()
        task_sequence.pop()
    elif tasks_time <= 180:
        rubber_duckies['Big Blue Rubber Ducky'] += 1
        time_sequence.popleft()
        task_sequence.pop()
    elif tasks_time <= 240:
        rubber_duckies['Small Yellow Rubber Ducky'] += 1
        time_sequence.popleft()
        task_sequence.pop()
    else:
        task_sequence[-1] -= 2
        time_sequence.append(time_sequence.popleft())

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print(f'Darth Vader Ducky: {rubber_duckies["Darth Vader Ducky"]}\n\
Thor Ducky: {rubber_duckies["Thor Ducky"]}\n\
Big Blue Rubber Ducky: {rubber_duckies["Big Blue Rubber Ducky"]}\n\
Small Yellow Rubber Ducky: {rubber_duckies["Small Yellow Rubber Ducky"]}')
