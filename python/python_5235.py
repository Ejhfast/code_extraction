# every element of list is True boolean
values = map(compare, new_subjects.values())
len([x for x in values if x]) == len(values) - 1
