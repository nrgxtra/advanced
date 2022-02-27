from collections import deque

males = list(map(int, input().split()))
females = deque(map(int,input().split()))
successful = 0
while males and females:
    first_male = males.pop()
    first_female = females.popleft()
    if first_male <= 0:
        continue
    if first_female <= 0:
        continue
    if first_male % 25 == 0:
        if len(males) >= 1:
            males.pop()
            if males:
                first_male = males.pop()
            else:
                break
        else:
            break
    if first_female % 25 == 0:
        if len(females) >= 1:
            females.popleft()
            if females:
                first_female = females.popleft()
            else:
                break
        else:
            break
    if first_male == first_female:
        successful += 1
    else:
        first_male -= 2
        if first_male > 0:
            males.append(first_male)

print(f"Matches: {successful}")
if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")

else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")

else:
    print("Females left: none")

