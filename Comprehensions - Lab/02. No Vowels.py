forbiden = ['a', 'o', 'u', 'e', 'i']

result = [x for x in input() if x.lower() not in forbiden]
print(''.join(result))


