from collections import deque


def solve(people, n):
    people = deque(people)
    i = 0
    while people:
        person = people.popleft()
        i += 1
        if i == n:
            if len(people) > 0:
                print(f'Removed {person}')
                i = 0
            else:
                print(f'Last is {person}')
                i = 0
        else:
            people.append(person)


solve(input().split(), int(input()))
