n = int(input())

matrix = []
plane_pos = []
target_count = 0

dirs = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

for row in range(n):
    line = input().split()
    if 'p' in line:
        plane_pos = [row, line.index('p')]
    if 't' in line:
        target_count += 1
    matrix.append(line)
m = int(input())
loose = True
for _ in range(m):
    tokens = input().split()
    action = tokens[0]
    direction = tokens[1]
    steps = int(tokens[2])
    if action == 'move':
        pl_row = int(plane_pos[0])
        pl_col = int(plane_pos[1])
        dir_row = int(dirs[direction][0])
        dir_col = int(dirs[direction][1])
        d_row = pl_row
        d_col = pl_col
        for _ in range(steps):
            d_row += dir_row
            d_col += dir_col
        if 0 <= d_row < len(matrix) and 0 <= d_col < len(matrix) and matrix[d_row][d_col] == '.':
            matrix[pl_row][pl_col] = '.'
            matrix[d_row][d_col] = 'p'
            plane_pos = [d_row, d_col]
    elif action == 'shoot':
        plane_row = int(plane_pos[0])
        plane_col = int(plane_pos[1])
        dir_row = int(dirs[direction][0])
        dir_col = int(dirs[direction][1])
        d_row = plane_row
        d_col = plane_col
        for _ in range(steps):
            d_row += dir_row
            d_col += dir_col
        if 0 <= d_row < len(matrix) and 0 <= d_col < len(matrix):
            if matrix[d_row][d_col] == 't':
                target_count -= 1
            matrix[d_row][d_col] = 'x'
            if target_count == 0:
                print(f"Mission accomplished! All {target_count} targets destroyed.")
                loose = False
                break
if loose:
    print(f"Mission failed! {target_count} targets left.")
[print(' '.join(row)) for row in matrix]
