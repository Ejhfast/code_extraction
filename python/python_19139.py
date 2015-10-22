# Combining Rows of Lists in Column containing Integers with Python
from itertools import chain
set(chain.from_iterable(df1['col1']))
