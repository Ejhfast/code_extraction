# pythonic way to sort a SortedDict
sorted_dict.keyOrder = [key[1] for key in sorted((v['priority'],k) for k,v in sorted_dict.items())]
