rows_count = int(input())
matrix = [list(map(int, input().split(', '))) for x in range(rows_count)]

primary = [matrix[row][col] for row in range(rows_count) for col in range(rows_count) if row == col]
secondary = [matrix[row][col] for row in range(rows_count) for col in range(rows_count) if row == rows_count - col - 1]
print(f"First diagonal: {str(primary)[1:-1]}. Sum: {sum(primary)}")
print(f"Second diagonal: {str(secondary)[1:-1]}. Sum: {sum(secondary)}")

