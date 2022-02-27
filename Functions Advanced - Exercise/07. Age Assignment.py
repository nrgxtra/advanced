def age_assignment(*args, **kwargs):
    name_dd = dict()
    for el in kwargs:
        for name in args:
            if el in name:
                name_dd[name] = kwargs[el]
    return name_dd


print(age_assignment("Peter", "George", G=26, P=19))
