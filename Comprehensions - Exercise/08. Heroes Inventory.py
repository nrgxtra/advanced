names = input().split(', ')
dd = {name: {} for name in names}
while True:
    command = input()
    if command == 'End':
        break
    info = command.split('-')
    name = info[0]
    weapon = info[1]
    cost = int(info[2])
    if name in dd:
        if weapon not in dd[name]:
            dd[name][weapon] = cost

[print(f'{name} -> Items: {len(dd[name])}, Cost: {sum(dd[name].values())}') for name in dd]

