
rows_count, columns_count = input().split(' ')
matrix = []
for _ in range(int(rows_count)):
    matrix.append(input().split(' '))
counter = 0
for i in range(int(rows_count)):
    for j in range(int(columns_count)):
        current_element = matrix[i][j]
        if i+1 < int(rows_count) and j+1 < int(columns_count):
            if current_element == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                counter += 1
print(counter)



