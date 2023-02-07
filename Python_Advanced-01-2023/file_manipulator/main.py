from os import remove

while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    elif command[0] == 'Create':
        file = open(command[1], 'w')
        file.close()
    elif command[0] == 'Add':
        file = open(command[1], 'a')
        file.write(command[2]+'\n')
        file.close()
    elif command[0] == 'Replace':
        try:
            file = open(command[1], 'r')
            text = file.read()
            file.close()
            text = text.replace(command[2], command[3])
            file = open(command[1], 'w')
            file.write(text)
            file.close()
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == 'Delete':
        try:
            remove(command[1])
        except FileNotFoundError:
            print("An error occurred")
