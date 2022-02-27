n = int(input())

even = set()
odd = set()

for i in range(1, n+1):
    name = input()
    number = [ord(x) for x in name]
    sum_of_name = sum(number)
    result = int(sum_of_name/i)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)
sum_of_even = sum(even)
sum_of_odd = sum(odd)
result = []
if sum_of_even == sum_of_odd:
    uni = odd | even
    result = [str(x) for x in uni]
    print(', '.join(result))
elif sum_of_odd > sum_of_even:
    new = odd.difference(even)
    result = [str(x) for x in new]
    print(', '.join(result))
else:
    newest = odd.symmetric_difference(even)
    result = [str(x) for x in newest]
    print(', '.join(result))
