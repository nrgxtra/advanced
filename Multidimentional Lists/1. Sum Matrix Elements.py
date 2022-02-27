#
# rows, columns = map(int, input().split(", "))
# matrix = []
# for _ in range(rows):
#     matrix.append(list(map(int, input().split(", "))))
# rows_sum = 0
# for el in matrix:
#     rows_sum += sum(el)
# print(rows_sum)
# print(matrix)

def read_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split(", "))))
    return matrix


def sum_matrix(matrix):
    rows_sum = 0
    for el in matrix:
        rows_sum += sum(el)
    return rows_sum


rows, columns = map(int, input().split(", "))
matrix = read_matrix(rows, columns)
print(sum_matrix(matrix))
print(matrix)

