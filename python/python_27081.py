# Test if python Counter is contained in another Counter
def contains(container, contained):
    return all(container[x] &gt;= contained[x] for x in contained)
