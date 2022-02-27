n = int(input())

s = set()
for _ in range(n):
    elements = input().split(' ')
    for el in elements:
        s.add(el)
[print(x) for x in s]

