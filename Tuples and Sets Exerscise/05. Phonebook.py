phone_book = dict()
enough = False
while True:
    if enough:
        break
    command = input()
    if command == 'stop':
        break
    elif command == 'search':
        while True:
            person = input()
            if person == 'stop':
                enough = True
                break
            if person not in phone_book:
                print(f'Contact {person} does not exist.')
            else:
                print(f'{person} -> {phone_book[person]}')
    else:
        name, number = command.split('-')
        if name not in phone_book:
            phone_book[name] = ''
        phone_book[name] = number

