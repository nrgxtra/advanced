from collections import deque

def solve():
    liters = int(input())
    people = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people.append(person)
    while people:
        command = input()
        if command.startswith('refill'):
            liters += int(command.split()[1])
            continue
        else:
            person = people.popleft()
            demanding_litters = int(command)
            if liters < demanding_litters:
                print(f'{person} must wait')
            else:
                print(f'{person} got water')
                liters -= demanding_litters
    print(f'{liters} liters left')

solve()
