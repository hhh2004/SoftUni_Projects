factor = int(input())
count = int(input())
num = 0
multiples = []

for i in range(count):
    num += factor
    multiples.append(num)

print(multiples)
