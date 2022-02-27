def sort_numbers(*args):
    result = sorted(args[0])
    print(result)


sort_numbers(list(map(int, input().split())))
