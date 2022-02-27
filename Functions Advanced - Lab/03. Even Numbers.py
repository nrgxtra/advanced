def even_numbers(*args):
    result = [int(x) for x in args[0] if int(x) % 2 == 0]
    print(result)


even_numbers(input().split())
