from collections import deque

text = deque(input().split())

main_colors = {'red': 0, 'yellow': 0, 'blue': 0}
secondary_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
result = []
while text:
    cur_one = text.popleft()
    if text:
        cur_two = text.pop()
        mix1 = cur_one + cur_two

        mix2 = cur_two + cur_one
        if mix1 in main_colors:
            main_colors[mix1] += 1
            if mix1 not in result:
                result.append(mix1)
        elif mix1 in secondary_colors:
            if mix1 not in result:
                result.append(mix1)
        elif mix2 in main_colors:
            main_colors[mix2] += 1
            if mix2 not in result:
                result.append(mix2)
        elif mix2 in secondary_colors:
            if mix2 not in result:
                result.append(mix2)
        else:
            to_place1 = cur_one[:-1]
            to_place2 = cur_two[:-1]
            half = len(text) // 2
            text.insert(half, to_place1)
            text.insert(half+1, to_place2)
for color in result:
    if color in secondary_colors:
        needed1 = secondary_colors[color][0]
        needed2 = secondary_colors[color][1]
        if main_colors[needed1] == 0 or main_colors[needed2] == 0:
            result.remove(color)
print(result)



