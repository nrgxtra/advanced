text = input()
n = int(input())
matrix = []
p_pos = []

for i in range(n):
    r = list(input())
    if 'P' in r:
        row = i
        col = r.index('P')
        p_pos.append(row)
        p_pos.append(col)
    matrix.append(r)
moves = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
print(p_pos)
[print(row) for row in matrix]