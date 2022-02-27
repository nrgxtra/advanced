from collections import deque

customers = deque()
[customers.append(int(x)) for x in input().split(', ')]
cars = deque()
[cars.append(int(x)) for x in input().split(', ')]
total_time = 0
success = True

while True:
    if len(cars) == 0 and len(customers) > 0:
        success = False
        break
    if len(customers) == 0:
        break
    current_customer = customers.popleft()
    current_car = cars.pop()
    if current_car >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)
if success:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(str(x) for x in customers)}")


