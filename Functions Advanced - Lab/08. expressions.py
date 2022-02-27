import itertools
numbers = [x for x in input().split(', ')]
n = len(numbers)
perm = itertools.product('+-', repeat=n)

for p in perm:
    expression = ''.join(itertools.chain(*zip(p, numbers)))
    result = eval(expression)
    print(f"{expression}={result}")







