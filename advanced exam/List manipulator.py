from collections import deque


def list_manipulator(n, *args):
    n_s = [x for x in n]
    numbers = deque(n_s)
    arguments = deque(args)
    operation = arguments.popleft()
    where = arguments.popleft()
    rest = arguments
    if operation == 'add':
        nums = list(arguments)
        if where == 'beginning':
            for num in reversed(nums):
                numbers.appendleft(num)
        elif where == 'end':
            for num in nums:
                numbers.append(num)
    elif operation == 'remove':
        nums = list(arguments)
        if where == 'beginning':
            if nums:
                for num in nums:
                    for _ in range(num):
                        numbers.popleft()
            else:
                numbers.popleft()
        elif where == 'end':
            if rest:
                for num in nums:
                    for _ in range(num):
                        numbers.pop()
            else:
                numbers.pop()
    return list(numbers)

print(list_manipulator([1,2,3], "remove", "beginning", 2))








