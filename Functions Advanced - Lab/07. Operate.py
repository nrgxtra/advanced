def operate(op, *args):
    first, *rest = args
    result = first
    if op == '+':
        for el in rest:
            result += el
        return result
    elif op == '-':
        for el in rest:
            result -= el
        return result
    elif op == '/':
        for el in rest:
            result /= el
        return result
    elif op == '*':
        for el in rest:
            result *= el
        return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


