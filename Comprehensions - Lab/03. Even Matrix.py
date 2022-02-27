rows_count = int(input())
matrix = []
for _ in range(rows_count):
    matrix.append(map(int, input().split(', ')))
result = [[el for el in row if el%2==0] for row in matrix]
print(result)
