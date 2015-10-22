# Python - How to ensure all lengths of elements in a nested list are the same?
def evenlengthchecker(nestedlist):
    a = [len(i) for i in nestedlist]
    return len(set(a)) ==1
