def rounding(*args):
    result = []
    for el in args[0]:
        result.append(round(float(el)))
    return result


print(rounding(input().split()))
