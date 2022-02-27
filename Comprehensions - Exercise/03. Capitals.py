countries = input().split(', ')
capitals = input().split(', ')
dd = zip(countries, capitals)
result = {x: y for (x, y) in dd}

[print(f'{key} -> {value}') for (key, value) in result.items()]
