def print_even(n):
    evens = []
    for i in range(len(n)):
        current = int(n[i])
        if current % 2 == 0:
            evens.append(current)
    return evens


n = input().split()
print(print_even(n))

