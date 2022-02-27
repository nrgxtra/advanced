def permutations(index, values):
    if index >= len(values):
        print(''.join(values))
        return
    permutations(index + 1, values)
    for i in range(index + 1, len(values)):
        values[index], values[i] = values[i], values[index]
        permutations(index + 1, values)
        values[index], values[i] = values[i], values[index]


values = list(input())
permutations(0, values)

