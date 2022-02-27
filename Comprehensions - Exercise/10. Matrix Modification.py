rows_count = int(input())
matrix = []
for _ in range(rows_count):
    matrix.append(list(map(int, input().split())))
while True:
    command = input()
    if command == 'END':
        break
    tokens = command.split()
    operation = tokens[0]
    row = int(tokens[1])
    column = int(tokens[2])
    value = int(tokens[3])
    if operation == 'Add':
        if 0 <= row < rows_count and 0 <= column < rows_count:
            matrix[row][column] += value
        else:
            print('Invalid coordinates')
    elif operation == 'Subtract':
        if 0 <= row < rows_count and 0 <= column < rows_count:
            matrix[row][column] -= value
        else:
            print('Invalid coordinates')
[print(' '.join(map(str, x))) for x in matrix]

