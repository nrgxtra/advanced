from collections import deque
import math
text = deque(input().split())
ops = ["*", "+", "-", "/"]
result = deque()
for el in text:
    if el not in ops:
        result.append(el)
    else:
        if el == '*':
            temp_res = int(result.popleft())
            while result:
                temp_res *= int(result.popleft())
            result.append(temp_res)
        elif el == '+':
            temp_res = int(result.popleft())
            while result:
                temp_res += int(result.popleft())
            result.append(temp_res)
        elif el == '-':
            temp_res = int(result.popleft())
            while result:
                temp_res -= int(result.popleft())
            result.append(temp_res)
        elif el == '/':
            temp_res = int(result.popleft())
            while result:
                temp_res /= int(result.popleft())
            result.append(math.floor(temp_res))
print(result.popleft())
