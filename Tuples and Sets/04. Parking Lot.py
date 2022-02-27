uni_cars = set()
while True:
    command = input()
    if command == 'END':
        break
    else:
        direction, plate = command.split(', ')
        if direction == 'IN':
            uni_cars.add(plate)
        elif direction == 'OUT':
            if plate in uni_cars:
                uni_cars.remove(plate)
if uni_cars:
    [print(x) for x in uni_cars]
else:
    print('Parking Lot is Empty')



