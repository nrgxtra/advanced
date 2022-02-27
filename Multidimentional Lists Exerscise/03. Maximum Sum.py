rows_count, columns_count = map(int, input().split(' '))

matrix = []
for _ in range(rows_count):
    matrix.append(list(map(int, input().split())))
the_sum = None
best_start = None
rc = len(matrix)
cc = len(matrix[0])
for i in range(rc - 2):
    for j in range(cc - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
                      matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
                      matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if the_sum:
            if the_sum < current_sum:
                the_sum = current_sum
                best_start = i, j

        else:
            the_sum = current_sum
            best_start = i, j

row, col = best_start
max_sub_matrix = [
    [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
    [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
    [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
]

print(f'Sum = {the_sum}')

[print(' '.join(map(str, row))) for row in max_sub_matrix]
