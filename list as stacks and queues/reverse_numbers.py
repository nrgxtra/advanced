n = [x for x in input().split()]
result = []
for _ in range(len(n)):
    current = n.pop()
    result.append(current)

print(' '.join(result))



