# Comparing lists of dictionaries
def get_new_failures(list1, list2):
    check = set([(d['classname'], d['testname']) for d in list2])
    return [d for d in list1 if (d['classname'], d['testname']) not in check]
