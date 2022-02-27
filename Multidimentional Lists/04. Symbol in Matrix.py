# def found_symbol(construction):
#     n = construction
#     matrix = []
#     for _ in range(n):
#         matrix.append([ch for ch in input()])
#     symbol = input()
#     found = False
#     for i in range(n):
#         if found:
#             break
#         for j in range(n):
#             if matrix[i][j] == symbol:
#                 print(f'({i}, {j})')
#                 found = True
#                 break
#     if not found:
#         print(f"{symbol} does not occur in the matrix")
#
#
# found_symbol(int(input()))
def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([ch for ch in input()])
    return matrix


def find_char(matrix, char):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_char = matrix[i][j]
            if current_char == char:
                return (i, j)
    return f'{char} does not occur in the matrix'


matrix = read_matrix(int(input()))
print(find_char(matrix, input()))
