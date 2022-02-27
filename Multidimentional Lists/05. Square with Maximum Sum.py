rows_count, columns_count = map(int, input().split(', '))
matrix = []
for _ in range(rows_count):
    matrix.append(list(map(int, input().split(', '))))
best_sum = None
best_start = None
for row in range(rows_count - 1):
    for col in range(int(columns_count) - 1):
        current_sum = matrix[row][col] + \
                      matrix[row][col + 1] + \
                      matrix[row + 1][col] + \
                      matrix[row + 1][col + 1]
        if best_sum:
            if best_sum < current_sum:
                best_sum = current_sum
                best_start = (row, col)

        else:
            best_sum = current_sum
            best_start = (row, col)

row, col = best_start
sub_matrix = [[matrix[row][col],
              matrix[row][col + 1]],
              [matrix[row + 1][col],
              matrix[row + 1][col + 1]]]
[print(' '.join(map(str, row))) for row in sub_matrix]
print(best_sum)
