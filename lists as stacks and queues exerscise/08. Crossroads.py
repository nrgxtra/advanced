from collections import deque

gl_duration = int(input())
window = int(input())
cars = deque()
command = input()
car_counter = 0
car_hit = ''
detail_hit = ''
initial_window = window
initial_gl_duration = gl_duration
success = True
while command != 'END' and success:
    if command == 'green':
        while gl_duration > 0 and cars:
            current_car = cars.popleft()
            car_counter += 1
            element_counter = len(current_car)
            for el in range(len(current_car)):
                if gl_duration > 0 and element_counter > 0:
                    gl_duration -= 1
                    element_counter -= 1
                else:
                    if element_counter > 0:
                        for i in range(len(current_car) - (len(current_car) - element_counter)):
                            if window > 0:
                                element_counter -= 1
                                window -= 1
                            else:
                                break
                        if element_counter > 0:
                            success = False
                            car_hit = current_car
                            details = [x for x in current_car]
                            detail_hit = details[el+initial_window]
                            car_counter -= 1
                            break
    else:
        car = command
        cars.append(car)
    command = input()
    gl_duration = initial_gl_duration
if success:
    print('Everyone is safe.')
    print(f'{car_counter} total cars passed the crossroads.')
else:
    print('A crash happened!')
    print(f'{car_hit} was hit at {detail_hit}.')


