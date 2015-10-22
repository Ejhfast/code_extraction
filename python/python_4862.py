# Python - return a region of a list based on calculated percentages
def split_list(mylist, *args):
    ilist = map(lambda p : int(p * len(mylist) / 100.0), args) + [len(mylist)]
    return reduce(lambda l, v : [l[0] + [mylist[l[1]:v]], v], ilist, [[],0])[0]
