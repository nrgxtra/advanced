from collections import deque
food = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)
print(biggest_order)
while orders:
    demanded = orders.popleft()
    if food >= demanded:
        food -= demanded
    else:
        orders.appendleft(demanded)
        print(f"Orders left: {' '.join([str(x) for x in list(orders)])}")
        break
if not orders:
    print('Orders complete')
