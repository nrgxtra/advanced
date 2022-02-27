n = int(input())
matrix = []
b_pos = []
row = 0
col = 0
for i in range(n):
    r = list(input())
    if 'S' in r:
        row = i
        col = r.index('S')
    if 'B' in r:
        b_row = i
        b_col = r.index('B')
        b_pos.append([b_row, b_col])
    matrix.append(r)
moves = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
food = 0
out = False
while food < 10 and not out:
    move = input()
    next_row = row + moves[move][0]
    next_col = col + moves[move][1]
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        matrix[row][col] = '.'
        out = True
        break
    else:
        if matrix[next_row][next_col] == '*':
            food += 1
            matrix[next_row][next_col] = 'S'
            matrix[row][col] = '.'
            row = next_row
            col = next_col
        elif matrix[next_row][next_col] == 'B':
            if [next_row, next_col] == b_pos[0]:
                matrix[row][col] = '.'
                matrix[next_row][next_col] = '.'
                row = b_pos[1][0]
                col = b_pos[1][1]
                matrix[row][col] = 'S'
            elif [next_row, next_col] == b_pos[1]:
                matrix[row][col] = '.'
                matrix[next_row][next_col] = '.'
                row = b_pos[0][0]
                col = b_pos[0][1]
                matrix[row][col] = 'S'
        elif matrix[next_row][next_col] == '-':
            matrix[next_row][next_col] = 'S'
            matrix[row][col] = '.'
            row = next_row
            col = next_col

if out:
    print("Game over!")
    print(f"Food eaten: {food}")
else:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food}")
for row in matrix:
    print(''.join(row))
