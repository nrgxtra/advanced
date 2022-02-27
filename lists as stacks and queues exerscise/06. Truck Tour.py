from collections import deque

n = int(input())
pumps = deque()
for _ in range(n):
    pumps.append([int(x) for x in input().split()])
idx = 0
fuel = 0
while pumps:
    temporary = []
    for _ in range(n):
        current = pumps.popleft()
        temporary.append(current)
        fuel += current[0]
        distance = current[1]
        if fuel < distance:
            idx += len(temporary)
            [pumps.append(x) for x in temporary]
            fuel = 0
            break
        else:
            fuel -= distance

print(idx)






