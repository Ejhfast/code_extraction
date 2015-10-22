# django create list from a queryset list
my_dict = {}
for obj in my_objects:
    my_dict.setdefault(obj.year, []).append(obj)
