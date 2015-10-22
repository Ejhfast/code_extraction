# Python: Syntax error in list comprehension statement
missing_buckets = [x for x in timebuckets if ((x not in found_tenors) and (x == '1y' or  x[-1] != 'y'))]
                   ^^^^^
