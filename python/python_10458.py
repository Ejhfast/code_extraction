# Python: Mulitple yield statements in generator
def rem0(data):
    for x in data:
        yield x.lstrip('0').replace(".0", ".")
