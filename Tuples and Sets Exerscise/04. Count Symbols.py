text = input()

dd = dict()

for item in text:
    if item not in dd:
        dd[item] = 0
    dd[item] += 1
for el, count in sorted(dd.items()):
    print(f'{el}: {count} time/s')
