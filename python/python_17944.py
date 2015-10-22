# Converting from nested lists to a delimited string
def lists_to_dyn(lst):
    return '|'.join(';'.join(','.join(lst3) for lst3 in lst2) for lst2 in lst)
