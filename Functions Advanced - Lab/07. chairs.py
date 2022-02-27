def combinations(values, h, comb=[]):
    if len(comb) == h:
        print(', '.join(comb))
        return
    for i in range(len(values)):
        x = values[i]
        comb.append(x)
        combinations(values[i+1:], h, comb)
        comb.pop()


values = input().split(', ')
h = int(input())
combinations(values, h)
