def get_magic_triangle(n):
    matrix = []
    for i in range(1, n+1):
        matrix.append([1*i for x in range(i)])
    print(matrix)


get_magic_triangle(5)
