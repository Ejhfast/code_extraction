# Python: Sort list using another list order, having different lengths, and without 'sorted'
[x for x in correct_order if x in messed_order] + [x for x in messed_order if x not in correct_order]
