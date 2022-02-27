rows_count = int(input())
matrix = []
for _ in range(rows_count):
    matrix.append(map(int, input().split(', ')))
new_matrix = [x for row in matrix for x in row]
print(new_matrix)
