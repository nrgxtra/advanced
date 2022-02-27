rows_count, columns_count = map(int, (input().split(' ')))
matrix = []
for _ in range(rows_count):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break
    else:
        tokens = command.split()
        if tokens[0] == 'swap' and len(tokens) == 5:
            r1 = int(tokens[1])
            c1 = int(tokens[2])
            r2 = int(tokens[3])
            c2 = int(tokens[4])
            if (r1 > rows_count - 1 or r2 > rows_count - 1) or (c1 > columns_count - 1 or c2 > columns_count - 1):
                print('Invalid input!')
            else:
                first_element = matrix[r1][c1]
                second_element = matrix[r2][c2]
                matrix[r1].pop(c1)
                matrix[r1].insert(c1, second_element)
                matrix[r2].pop(c2)
                matrix[r2].insert(c2, first_element)

                [print(' '.join(row)) for row in matrix]
        else:
            print('Invalid input!')

