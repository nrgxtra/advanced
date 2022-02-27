def operate(operator, *args):
    return eval(str(operator).join([str(x) for x in args]))


print(operate("+", 2, 3, 4))

