import os
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    action = tokens[0]
    if action == 'Create':
        f_name = tokens[1]
        with open(f_name, 'w') as fh:
            pass
    elif action == 'Add':
        f_name = tokens[1]
        content = f'{tokens[2]}\n'
        with open(f_name, 'a') as fh:
            fh.write(content)
    elif action == 'Replace':
        f_name = tokens[1]
        old = tokens[2]
        new = tokens[3]
        try:
            with open(f_name, 'a') as fh:
                f_name.replace(old, new)
        except FileNotFoundError:
            print('An error occurred')
    elif action == 'Delete':
        f_name = tokens[1]
        if os.path.exists(f_name):
            os.remove(f_name)
        else:
            print('An error occurred')




