def diag_sum(matrix_borders):
    n = matrix_borders
    matrix = []
    diagonal = 0
    for i in range(n):
        matrix.append([int(x) for x in input().split(' ')])
        for j in range(n):
            diagonal += matrix[i][i]
            break
    print(diagonal)


diag_sum(int(input()))
