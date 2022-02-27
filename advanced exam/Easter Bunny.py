n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split())

b_r = 0
b_c = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'B':
            b_r = i
            b_c = j
best = {}
moves = ['left', 'right', 'up', 'down']

for move in moves:
    result = 0
    if move == 'left':
        x = b_r
        y = b_c - 1
        while 0 <= x < n and 0 <= y < n:
            if matrix[x][y] == 'X':
                break
            number = int(matrix[x][y])
            result += number
            y -= 1
        best[move] = result
    elif move == 'right':
        x = b_r
        y = b_c + 1
        while 0 <= x < n and 0 <= y < n:
            if matrix[x][y] == 'X':
                break
            number = int(matrix[x][y])
            result += number
            y += 1
        best[move] = result
    elif move == 'up':
        x = b_r - 1
        y = b_c
        while 0 <= x < n and 0 <= y < n:
            if matrix[x][y] == 'X':
                break
            number = int(matrix[x][y])
            result += number
            x -= 1
        best[move] = result
    elif move == 'down':
        x = b_r + 1
        y = b_c
        while 0 <= x < n and 0 <= y < n:
            if matrix[x][y] == 'X':
                break
            number = int(matrix[x][y])
            result += number
            x += 1
        best[move] = result
res = dict(sorted(best.items(), key= lambda x: -x[1]))
best_direction = ''
best_value = 0
for k, v in res.items():
    best_direction = k
    best_value = v
    break
print(best_direction)
dirs = {'left': [0, -1], 'right': [0, 1], 'up': [-1, 0], 'down': [1, 0]}
x = b_r + dirs[best_direction][0]
y = b_c + dirs[best_direction][1]
while 0 <= x < n and 0 <= y < n:
    if matrix[x][y] == 'X':
        break
    print([x, y])
    b_r = x
    b_c = y
    x = b_r + dirs[best_direction][0]
    y = b_c + dirs[best_direction][1]
print(best_value)



