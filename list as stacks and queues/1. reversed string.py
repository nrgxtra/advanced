# def solve(str):
#     s = []
#     for ch in str:
#         s.append(ch)
#     reversed = ''
#     while s:
#         reversed += s.pop()
#     return reversed
# print(solve(input()))

def solve2(str):
    return str[::-1]
print(solve2(input()))
