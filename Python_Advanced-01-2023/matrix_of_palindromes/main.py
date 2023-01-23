rows, columns = [int(x) for x in input().split()]
char = 97
for i in range(rows):
    print(' '.join([chr(char+i)+chr(char+j)+chr(char+i) for j in range(i, i+columns)]))
