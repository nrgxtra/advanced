from collections import deque
n, s, x = input().split(' ')
q = deque()
[q.append(int(x)) for x in input().split(' ')]
for i in range(int(s)):
    q.popleft()
if int(x) in q:
    print('True')
else:
    if q:
        q = sorted(q)
        print(q[0])
    else:
        print('0')

