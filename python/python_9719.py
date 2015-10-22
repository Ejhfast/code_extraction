# Function code. Python 2.7
def reverse_section(alist, start, end):
    return alist[:start] + list(reversed(alist[start:end+1])) + alist[end+1:]
