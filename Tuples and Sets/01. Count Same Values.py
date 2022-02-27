
def solve(values):
    numbers = dict()
    for element in values:
        if element not in numbers:
            numbers[element] = 0
        numbers[element] += 1
    for key, value in numbers.items():
        print(f'{key} - {value} times')


solve([float(x) for x in input().split(' ')])
