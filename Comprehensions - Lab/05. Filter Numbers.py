def valid(number):
    return any([number % el == 0 for el in numbers])


start = int(input())
end = int(input())
checked = [j for j in range(start, end + 1)]
numbers = [h for h in range(2, 21)]
result = [x for x in checked if valid(x)]
print(result)
