def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    numbers = [int(x) for x in nums]
    if command == 'even':
        return [x for x in numbers if x % 2 == 0]
    elif command == 'odd':
        return [x for x in numbers if x % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))