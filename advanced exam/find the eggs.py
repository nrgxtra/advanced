
def find_strongest_eggs(*args):
    eggs = args[0]
    div = args[1]
    res = []
    strongest = []
    is_strong = True
    n = div
    for _ in range(n):
        res.append([])
    for i in range(1):
        if div == 1:
            res.append(eggs)
            break
        else:
            for j in range(len(eggs)):
                if j % 2 == 0:
                    res[0].append(eggs[j])
                else:
                    res[1].append(eggs[j])
    if div == 1:
        middle = len(res[1]) // 2
        mid = res[1][middle]
        left = list(res[1][:middle])
        right = list(reversed(res[1][middle + 1:]))
        while left and right:
            is_strong = True
            l = left.pop()
            r = right.pop()
            if mid <= l or mid <= r or r <= l:
                is_strong = False
                break
        if is_strong:
            strongest.append(mid)
    else:
        for el in res:
            middle = len(el) // 2
            mid = el[middle]
            left = list(el[:middle])
            right = list(reversed(el[middle+1:]))
            while left and right:
                is_strong = True
                l = left.pop()
                r = right.pop()
                if mid <= l or mid <= r or r <= l:
                    is_strong = False
                    break
            if is_strong:
                strongest.append(mid)

    return strongest


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))





