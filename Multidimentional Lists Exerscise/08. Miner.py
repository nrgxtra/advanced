rows_count = int(input())
field = []
commands = []

[commands.append(x) for x in input().split(' ')]
for _ in range(rows_count):
    field.append([])
    [field[-1].append(x) for x in input().split()]
coals = 0
current_coal = 0
for row in field:
    sub_sum = row.count('c')
    coals += sub_sum
initial_start = []

for i in range(len(field)):
    for j in range(len(field)):
        if field[i][j] == 's':
            initial_start.append(i)
            initial_start.append(j)
initial_row = initial_start[0]
initial_column = initial_start[1]
current_position = field[initial_row][initial_column]
row = initial_row
column = initial_column
end_or_mineall = False
for command in commands:
    if command == 'left':
        if column - 1 >= 0:
            row = row
            column = column-1
            if field[row][column] == 'e':
                print(f'Game over! ({row}, {column})')
                end_or_mineall = True
                break
            elif field[row][column] == 'c':
                current_coal += 1
                field[row][column] = '*'
                if current_coal == coals:
                    print(f"You collected all coals! ({row}, {column})")
                    end_or_mineall = True
                    break
    elif command == 'right':
        if column + 1 < len(field):
            row = row
            column = column + 1
            if field[row][column] == 'e':
                print(f'Game over! ({row}, {column})')
                end_or_mineall = True
                break
            elif field[row][column] == 'c':
                current_coal += 1
                field[row][column] = '*'
                if current_coal == coals:
                    print(f"You collected all coals! ({row}, {column})")
                    end_or_mineall = True
                    break
    elif command == 'up':
        if row - 1 >= 0:
            row = row - 1
            column = column
            if field[row][column] == 'e':
                print(f'Game over! ({row}, {column})')
                end_or_mineall = True
                break
            elif field[row][column] == 'c':
                current_coal += 1
                field[row][column] = '*'
                if current_coal == coals:
                    print(f"You collected all coals! ({row}, {column})")
                    end_or_mineall = True
                    break
    elif command == 'down':
        if row + 1 < len(field):
            row = row + 1
            column = column
            if field[row][column] == 'e':
                print(f'Game over! ({row}, {column})')
                end_or_mineall = True
                break
            elif field[row][column] == 'c':
                current_coal += 1
                field[row][column] = '*'
                if current_coal == coals:
                    print(f"You collected all coals! ({row}, {column})")
                    end_or_mineall = True
                    break
if not end_or_mineall:
    coals_left = coals - current_coal
    print(f"{coals_left} coals left. ({row}, {column})")

