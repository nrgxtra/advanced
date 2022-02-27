n, s, x = input().split(' ')
st = []
[st.append(int(x)) for x in input().split(' ')]
for j in range(int(s)):
    st.pop()
if int(x) in st:
    print('True')
else:
    st = sorted(st)
    if st:
        print(st[0])
    else:
        print('0')




