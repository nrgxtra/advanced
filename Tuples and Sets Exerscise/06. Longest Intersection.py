n = int(input())
largest = 0
longest = []
for _ in range(n):
    s1 = set()
    s2 = set()
    basi = input().split('-')
    for el in range(len(basi)):
        if el % 2 == 0:
            num1, num2 = basi[el].split(',')
            for i in range(int(num1), int(num2)+1):
                s1.add(i)
        else:
            num1, num2 = basi[el].split(',')
            for i in range(int(num1), int(num2) + 1):
                s2.add(i)
        result = s1.intersection(s2)
        if len(result) > largest:
            largest = len(result)
            longest = [x for x in result]

print(f'Longest intersection is {longest} with length {largest}')





