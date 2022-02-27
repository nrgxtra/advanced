def numbers_searching(*args):
    numbers = [int(x) for x in args]
    smallest = min(numbers)
    biggest = max(numbers)
    missing = 0
    desired = []
    repeated = []
    for i in range(smallest, biggest + 1):
        desired.append(i)
    for n in desired:
        if n not in numbers:
            missing = n
    for el in numbers:
        res = numbers.count(el)
        if res > 1:
            repeated.append(el)
    ordered_repeated = sorted(set(repeated))
    result = [missing, ordered_repeated]
    return result



