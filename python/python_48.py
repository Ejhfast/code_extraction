# Find out number of capture groups in Python regular expressions
def num_groups(regex):
    return re.compile(regex).groups
