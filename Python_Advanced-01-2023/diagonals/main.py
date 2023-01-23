n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n-i-1] for i in range(n)]
print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
