count_of_presents = int(input())
matrix_size = int(input())
matrix = []
s_pos = []
nice_kids_count = 0
for i in range(matrix_size):
    row = input().split()
    if 'S' in row:
        s_pos = [i, row.index('S')]
    if 'V' in row:
        nice_kids_count += row.count('V')
    matrix.append(row)
directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

while True:
    command = input()
    if command == 'Christmas morning' or count_of_presents <= 0:
        break
    nr = s_pos[0]+directions[command][0]
    nc = s_pos[1]+directions[command][1]
    if 0 <= nr < matrix_size and 0 <= nc < matrix_size:
        next_row = nr
        next_col = nc
        if matrix[next_row][next_col] == 'V':
            count_of_presents -= 1
        elif matrix[next_row][next_col] == 'C':
            for move in directions:
                n_pos = matrix[next_row + directions[move][0]][next_col + directions[move][1]]
                if n_pos == 'V' or n_pos == 'X':
                    count_of_presents -= 1
                matrix[next_row + directions[move][0]][next_col + directions[move][1]] = '-'
                if count_of_presents == 0:
                    break
        matrix[nr][nc] = 'S'
        matrix[s_pos[0]][s_pos[1]] = '-'
        s_pos = [nr, nc]
        if count_of_presents == 0:
            break

nice_kids_left = 0
for row in matrix:
    if 'V' in row:
        nice_kids_left += row.count('V')

if count_of_presents <= 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")
[print(' '.join(row)) for row in matrix]
if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")



