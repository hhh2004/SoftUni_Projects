password = input()
is_valid = True

if len(password) < 6 or len(password) > 10:  # checks if the password is from 6 to 10 characters
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not password.isalnum():  # checks if the password is alphanumeric
    is_valid = False
    print("Password must consist only of letters and digits")

digits = 0
for char in password:       # counts digits in password and checks if they are 2 or more
    if char.isnumeric():
        digits += 1
    if digits == 2:
        break
if digits < 2:
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")


