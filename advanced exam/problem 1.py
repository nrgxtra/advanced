from collections import deque
males = list(map(int, input().split()))
females = deque(map(int,input().split()))

successful = 0
while males and females:
    fm = males[-1]
    ff = females[0]
    if fm <= 0:
        males.pop()
        continue
    if ff <= 0:
        females.popleft()
        continue
    if fm % 25 == 0:
        males.pop()
        males.pop()
        continue
    if ff % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if ff == fm:
        males.pop()
        females.popleft()
        successful += 1
        males = [x for x in males if x > 0]
        females = deque([x for x in females if x > 0])
    else:
        females.popleft()
        males[-1] -= 2
        males = [x for x in males if x > 0]

print(f"Matches: {successful}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(list(map(str, reversed(males))))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(list(map(str, females)))}")


