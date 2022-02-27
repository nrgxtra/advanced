n, m = input().split(' ')
set1 = set()
set2 = set()
for _ in range(int(n)):
    number = int(input())
    set1.add(number)
for _ in range(int(m)):
    number = int(input())
    set2.add(number)
[print(x) for x in set2 and set1 if x in set2 and set1]
