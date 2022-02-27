def read_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix


def sum_columns(matrix):
    current_column_sum = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            current_column_sum += matrix[j][i]
        print(current_column_sum)
        current_column_sum = 0
    return


rows, columns = map(int, input().split(', '))
matrix = read_matrix(rows, columns)
sum_columns(matrix)





