from triangle import math_ops

expresion = input()
result = math_ops.execute(*math_ops.pars_expr(expresion))
print(f'{result:.2f}')

