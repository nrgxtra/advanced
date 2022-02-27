def spread_bunnies(lair, rows, columns):
    b_ees = []
    for i in range(rows):
        for j in range(columns):
            if lair[i][j] == 'B':
                b_ees.append([i, j])
    for b in b_ees:
        i = b[0]
        j = b[1]
        if i - 1 >= 0:
            lair[i - 1][j] = 'B'
        if i + 1 < rows:
            lair[i + 1][j] = 'B'
        if j - 1 >= 0:
            lair[i][j - 1] = 'B'
        if j + 1 < columns:
            lair[i][j + 1] = 'B'

    return lair


rows, columns = map(int, input().split(' '))
lair = []
for _ in range(rows):
    lair.append([])
    [lair[-1].append(x) for x in input()]
directions = [x for x in input()]
position = []
for i in range(rows):
    for j in range(columns):
        if lair[i][j] == 'P':
            position.append(i)
            position.append(j)
            break
initial_row = position[0]
initial_column = position[1]
row = initial_row
column = initial_column
for move in directions:
    spread_bunnies(lair, rows, columns)
    if move == 'L':
        if column - 1 >= 0:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            row = row
            column = column - 1
            if lair[row][column] == 'B':
                [print(''.join(row)) for row in lair]
                print(f"dead: {row} {column}")
                break
            else:
                lair[row][column] = 'P'
        else:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            [print(''.join(row)) for row in lair]
            print(f'won: {row} {column}')
            break
    if move == 'R':
        if column + 1 < columns:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            row = row
            column = column + 1
            if lair[row][column] == 'B':
                [print(''.join(row)) for row in lair]
                print(f"dead: {row} {column}")
                break
            else:
                lair[row][column] = 'P'
        else:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            [print(''.join(row)) for row in lair]
            print(f'won: {row} {column}')
            break
    if move == 'U':
        if row - 1 >= 0:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            row = row - 1
            column = column
            if lair[row][column] == 'B':
                [print(''.join(row)) for row in lair]
                print(f"dead: {row} {column}")
                break
            else:
                lair[row][column] = 'P'
        else:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            [print(''.join(row)) for row in lair]
            print(f'won: {row} {column}')
            break
    if move == 'D':
        if row + 1 < rows:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            row = row + 1
            column = column
            if lair[row][column] == 'B':
                [print(''.join(row)) for row in lair]
                print(f"dead: {row} {column}")
                break
            else:
                lair[row][column] = 'P'
        else:
            if lair[row][column] != 'B':
                lair[row][column] = '.'
            [print(''.join(row)) for row in lair]
            print(f'won: {row} {column}')
            break

