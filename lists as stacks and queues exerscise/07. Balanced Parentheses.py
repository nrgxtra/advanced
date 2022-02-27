
matches = {'(': ')', '{': '}', '[': ']'}
parentheses = input()
test = []
yes = True
for i in parentheses:
    if i in '({[':
        test.append(i)
    elif i in ')}]':
        if test:
            current = test[-1]
            if matches[current] == i:
                test.pop()
            else:
                yes = False
                break
        else:
            yes = False
            break

if yes:
    print('YES')
else:
    print('NO')
