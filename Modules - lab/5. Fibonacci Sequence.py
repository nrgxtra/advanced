import fibonacci
sequence = []
while True:
    command = input()
    if command == 'Stop':
        break
    elif command.startswith('Create Sequence'):
        n = int(command.split()[-1])
        sequence = fibonacci.create_sequence(n)
        [print(x, end=' ') for x in sequence]
        print()
    elif command.startswith('Locate'):
        number = int(command.split()[-1])
        try:
            position = sequence.index(number)
            print(f'The number - {number} is at index {position}')
        except ValueError:
            print(f'The number {number} is not in the sequence')

