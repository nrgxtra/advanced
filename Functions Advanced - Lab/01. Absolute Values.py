def f(*args):
    result = []
    print(args)
    for el in args[0]:
        result.append(abs(float(el)))
    print(result)


f(input().split())












