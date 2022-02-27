def check(row_idx, col_idx):
    existing = []
    if row_idx - 1 >= 0 and col_idx - 1 >= 0:
        existing.append([row_idx - 1, col_idx - 1])
    if row_idx - 1 >= 0:
        existing.append([row_idx - 1, col_idx])
    if row_idx - 1 >= 0 and col_idx + 1 < len(matrix):
        existing.append([row_idx - 1, col_idx + 1])
    if row_idx >= 0 and col_idx - 1 >= 0:
        existing.append([row_idx, col_idx - 1])
    if row_idx >= 0 and col_idx + 1 < len(matrix):
        existing.append([row_idx, col_idx + 1])
    if row_idx + 1 < len(matrix) and col_idx - 1 >= 0:
        existing.append([row_idx + 1, col_idx - 1])
    if row_idx + 1 < len(matrix):
        existing.append([row_idx + 1, col_idx])
    if row_idx + 1 < len(matrix) and col_idx + 1 < len(matrix):
        existing.append([row_idx + 1, col_idx + 1])
    return existing


rows_count = int(input())
matrix = []
for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])
explosion = [[int(x) for x in j.split(',')] for j in input().split()]
dead_cells = []
for bomb in explosion:
    row_idx = bomb[0]
    col_idx = bomb[1]
    current_bomb = matrix[row_idx][col_idx]
    current_strength = matrix[row_idx][col_idx]
    if current_bomb > 0:
        matrix[row_idx][col_idx] = 0
        existing_cells = check(row_idx, col_idx)
        for row in existing_cells:
            r_ind, c_ind = row
            current_cell = matrix[r_ind][c_ind]
            if current_cell > 0:
                matrix[r_ind][c_ind] -= current_strength
alive = 0
alive_cells = []
for row in matrix:
    for el in row:
        if el > 0:
            alive += 1
            alive_cells.append(el)
sum_alive_cells = sum(alive_cells)
print(f'Alive cells: {alive}')
print(f'Sum: {sum_alive_cells}')
new_matrix = [[str(x) for x in j] for j in matrix]
[print(' '.join(row)) for row in new_matrix]
