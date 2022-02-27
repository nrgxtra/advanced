def even_odd(command):
    numbers = [int(x) for x in input().split()]
    if command == 'Odd':
        odd = [x for x in numbers if x % 2 == 1]
        result = sum(odd) * len(numbers)
        print(result)
    elif command == 'Even':
        even = [x for x in numbers if x % 2 == 0]
        result = sum(even) * len(numbers)
        print(result)


even_odd(input())
