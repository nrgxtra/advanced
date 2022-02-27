n = int(input())
st = []
for i in range(n):
    query = input().split()
    if query[0] == '1':
        st.append(int(query[1]))
    elif query[0] == '2' and st:
        st.pop()
    elif query[0] == '3' and st:
        st_max = sorted(st)
        print(st_max[-1])
    elif query[0] == '4' and st:
        st_min = sorted(st)
        print(st_min[0])
if st:
    for i in range(len(st)-1):
        print(f'{st.pop()}, ', end='')
    print(st[-1])
