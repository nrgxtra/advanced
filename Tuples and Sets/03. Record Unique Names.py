def record_unique(n):

    s = set()
    for _ in range(int(n)):
        name = input()
        s.add(name)
    [print(x) for x in s]


record_unique(input())
