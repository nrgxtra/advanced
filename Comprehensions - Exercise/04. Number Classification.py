numbers = list(map(int, input().split(', ')))
positive = []
negative = []
even = []
odd = []
[positive.append(x) if x >= 0 else negative.append(x) for x in numbers]
[even.append(x) if x % 2 == 0 else odd.append(x) for x in numbers]
print(f"Positive: {str(positive)[1:-1]}")
print(f"Negative: {str(negative)[1:-1]}")
print(f"Even: {str(even)[1:-1]}")
print(f"Odd: {str(odd)[1:-1]}")


