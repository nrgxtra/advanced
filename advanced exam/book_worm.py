text = input()
n = int(input())
matrix = []
player_pos = []
for i in range(n):
    row = list(input())
    if 'P' in row:
        player_pos = [i, row.index('P')]
    matrix.append(row)
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
m = int(input())
for _ in range(m):
    command = input()
    row = player_pos[0]
    column = player_pos[1]
    next_row = row + directions[command][0]
    next_column = column + directions[command][1]
    if 0 <= next_row < n and 0 <= next_column < n:
        next_position = matrix[next_row][next_column]
        if next_position != '-':
            text += next_position
        matrix[row][column] = '-'
        matrix[next_row][next_column] = 'P'
        player_pos = [next_row, next_column]
    else:
        text = text[:-1]
print(text)
[print(''.join(x)) for x in matrix]

