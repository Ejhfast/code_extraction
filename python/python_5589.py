# How to remove a range from start to end enclusive from a list
def remove_section(alist, start, end):
    return alist[:start] + alist[end+1:]
