f = open('numbers.txt')
result = 0
for n in f:
    result += int(n)
print(result)
f.close()
