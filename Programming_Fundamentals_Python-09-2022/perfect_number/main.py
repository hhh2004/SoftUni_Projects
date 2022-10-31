number = int(input())
divisors = []

for i in range(number//2):
    if number % (i+1) == 0:
        divisors.append(i+1)

if number == sum(divisors):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
