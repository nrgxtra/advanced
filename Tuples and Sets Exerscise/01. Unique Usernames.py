n = int(input())
collection = set()
for _ in range(n):
    username = input()
    collection.add(username)
[print(x) for x in collection]
