users = {}
commands_num = int(input())
for _ in range(commands_num):
    command = input().split(' ')
    if command[0] == "register":
        if command[1] in users.keys():
            print(f"ERROR: already registered with plate number {users[command[1]]}")
        else:
            users[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0] == "unregister":
        if command[1] in users.keys():
            users.pop(command[1])
            print(f"{command[1]} unregistered successfully")
        else:
            print(f"ERROR: user {command[1]} not found")

for username in users.keys():
    print(f"{username} => {users[username]}")
