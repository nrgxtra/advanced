import math
n = int(input())
base = input()
if base == 'natural':
    print(f'{math.log(n):.2f}')
else:
    print(f'{math.log(n, int(base)):.2f}')

