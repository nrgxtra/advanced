def concatenate(*args):
    st = ''
    for el in args:
        st += el
    return st

print(concatenate("Soft", "Uni", "Is", "Great", "!"))