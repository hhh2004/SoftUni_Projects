old_version = int(''.join(input().split('.')))
new_version = '.'.join([num for num in str(old_version + 1)])
print(new_version)
