def solve(*args):
    min_number = min(args[0])
    max_number = max(args[0])
    summary = sum(args[0])
    print(f'The minimum number is {min_number}')
    print(f'The maximum number is {max_number}')
    print(f'The sum number is: {summary}')


solve(list(map(int, input().split())))
