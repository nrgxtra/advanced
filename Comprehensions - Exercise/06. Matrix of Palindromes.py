rows_count, columns_count = map(int, input().split(' '))


matrix = []
for i in range(rows_count):
    matrix.append([])
    for j in range(columns_count):
        fl = chr(i+97)
        sl = chr(i+j+97)
        tl = chr(i+97)
        matrix[-1].append([fl, sl, tl])
for k in range(len(matrix)):
    print()
    for h in range(len(matrix[0])):
        print(''.join(matrix[k][h]), end=' ')

