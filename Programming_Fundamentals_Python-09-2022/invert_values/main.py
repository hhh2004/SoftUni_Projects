numbers = input()
number_list = numbers.split(" ")
for i in range(len(number_list)):
    number_list[i] = -(int(number_list[i]))
print(number_list)
