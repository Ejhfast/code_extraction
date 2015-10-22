# how do I generate a cartesian product of several variables using python iterators?
import itertools
site_range=[0,1,2]
[x for x in itertools.product(site_range, repeat=len(site_range))]
