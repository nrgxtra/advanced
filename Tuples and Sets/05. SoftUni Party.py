reserv_list = set()
party_list = set()
command = input()
while command != 'PARTY':
    reserv_list.add(command)
    command = input()
if command == 'PARTY':
    command = input()
    while command != 'END':
        party_list.add(command)
        command = input()


diff = abs(len(reserv_list) - len(party_list))
print(diff)
losers = (reserv_list-party_list)
sort = sorted(losers)
for el in sort:
    print(el)

