usernames = input().split(', ')
for i in range(len(usernames)):
    if len(usernames[i]) < 3 or len(usernames[i]) > 16:
        continue

    clean_username = usernames[i].replace('-', '')
    clean_username = clean_username.replace('_', '')

    if not clean_username.isalnum():
        continue
    else:
        print(usernames[i])
