def get_magic_triangle(n):
    matrix = []

    for x in range(n):

        if x == 0:
            help_list = [1]
            matrix.append(help_list)
            continue
        if x == 1:
            help_list = [1, 1]
            matrix.append(help_list)
            continue

        help_list = [l for l in range(x + 1)]
        for y in range(1, x):
            help_list[0] = 1
            help_list[x] = 1
            help_list[y] = matrix[x - 1][y] + matrix[x - 1][y - 1]

        matrix.append(help_list)

    return matrix



get_magic_triangle(5)