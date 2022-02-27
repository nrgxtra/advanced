f = open('text.txt', 'r')
try:
    file = open('text.txt', 'r')
    print('here is your file')
except FileNotFoundError:
    print('No such file')

finally:
    print('exit')

