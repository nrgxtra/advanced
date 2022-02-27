def directions(r, c):
    left = r, c-1
    right = r, c+1
    up = r-1, c
    down = r+1, c
    lu = r-1, c-1
    ru = r-1, c+1
    ld = r+1, c-1
    rd = r+1, c+1
    direct = [left, right, up, down, lu, ru, ld, rd]
    return direct


def find_value(field):
    for k in range(len(field)):
        for h in range(len(field[k])):
            symbol = field[k][h]
            if symbol == 0:
                value = 0
                for el in directions(k, h):
                    r, c = el
                    if 0 <= r < len(field) and 0 <= c < len(field):
                        if field[r][c] == '*':
                            value += 1
                field[k][h] = value
    return field


n = int(input())
bomb_number = int(input())
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

for _ in range(bomb_number):
    coordinates = input()
    b_r = ''
    b_c = ''
    for i in range(len(coordinates)):
        if coordinates[i].isdigit():
            b_r += coordinates[i]
        elif i+1 < len(coordinates) and not coordinates[i+1].isdigit():
            rest = coordinates[i+1:]
            for el in rest:
                if el.isdigit():
                    b_c += el
            break
    row = int(b_r)
    col = int(b_c)
    matrix[row][col] = '*'

for row in find_value(matrix):
    res = list(map(str, row))
    print(' '.join(res))


