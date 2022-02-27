
def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(int(x) for x in (input().split(' '))))
    return n, matrix


def find_primary_secondary():
    n, matrix = read_matrix()
    primary = 0
    secondary = 0
    for row in range(n):
        for col in range(n):
            if row == col:
                primary += matrix[row][col]
    for row in range(n):
        for col in range(n):
            if row == n - col - 1:
                secondary += matrix[row][col]
    return primary, secondary


def find_difference():
    primary, secondary = find_primary_secondary()
    diff = abs(primary - secondary)
    return print(diff)


find_difference()



