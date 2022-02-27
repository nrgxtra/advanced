numbers = input().split('|')
digits = []
while numbers:
    digits.append(numbers.pop())
result = []
for i in range(len(digits)):
    current_element = digits[i]
    result.append([])
    for j in range(len(current_element)):
        current_item = current_element[j]
        if current_item != ' ':
            result[-1].append(current_item)
        else:
            result.append([])
for el in result:
    if el != []:
        print(''.join(el), end=' ')





