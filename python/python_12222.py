# Turning a string into a list with specifications
from itertools import groupby
my_string= "google"
[(c, len(list(i))) for c, i in groupby(my_string)]
