from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]

bombs = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
made_bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}


def making_success(mb):
    result = False
    count = 0
    for v in mb.values():
        if v >= 3:
            count += 1
    if count == 3:
        result = True
    return result


while effects and casings and not making_success(made_bombs):
    current_effect = effects[0]
    current_casing = casings[-1]
    mix = current_effect + current_casing
    if mix in bombs:
        made_bombs[bombs[mix]] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
if making_success(made_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if not effects:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join((str(i) for i in effects))}")
if not casings:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join((str(i) for i in casings))}")
for key, value in sorted(made_bombs.items()):
    print(f"{key}: {value}")

