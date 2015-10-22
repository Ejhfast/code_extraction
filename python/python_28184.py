# Error in sorting operation on dictionary
sorted_niwa = sorted(ids_seqs.items(), key = lambda val: int(val[0].split()[2]), reverse=False)
