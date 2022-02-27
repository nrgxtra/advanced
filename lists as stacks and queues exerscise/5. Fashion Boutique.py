box = [int(x) for x in input().split()]
rack_capacity = int(input())
counter = 0
while box:
    current = 0
    while current <= rack_capacity and box:
        item = box.pop()
        current += item
        if current > rack_capacity:
            box.append(item)
            break
    counter += 1
print(counter)




